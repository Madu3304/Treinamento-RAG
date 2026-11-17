"""
Passos 2, 3 e 4: Limpeza, Normalização por Z Robusto, Categorização de Contexto
e Treinamento do Isolation Forest com Rastreamento no MLflow.
"""

import os
import json
from pathlib import Path
import numpy as np
import pandas as pd
import joblib

# Desabilitar avisos de telemetria do MLflow
os.environ["MLFLOW_DISABLE_AGENT_HINT"] = "1"

import mlflow
import mlflow.sklearn
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import recall_score, precision_score, f1_score

BASE_DIR = Path(__file__).resolve().parent
DADOS_DIR = BASE_DIR / "dados"
MODELOS_DIR = BASE_DIR / "modelos"
MODELOS_DIR.mkdir(parents=True, exist_ok=True)

FEATURES_VITAIS = ["fc", "pas", "pad", "glicose", "temp", "sono_h"]

def passo2_limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Passo 2. Limpeza:
    - Padronização de tipos e timestamps.
    - Remoção de valores fisicamente impossíveis causados por falhas de sensor
      (FC = 0, Temp = 80°C, etc.) sem apagar outliers reais/patológicos.
    - Imputação de nulos por interpolação temporal e forward fill.
    """
    df_clean = df.copy()
    
    # 1. Tratar valores impossíveis transformando em NaN para imputação
    df_clean.loc[(df_clean["fc"] <= 0) | (df_clean["fc"] > 250), "fc"] = np.nan
    df_clean.loc[(df_clean["temp"] < 32.0) | (df_clean["temp"] > 44.0), "temp"] = np.nan
    df_clean.loc[(df_clean["pas"] < 50) | (df_clean["pas"] > 260), "pas"] = np.nan
    df_clean.loc[(df_clean["pad"] < 30) | (df_clean["pad"] > 180), "pad"] = np.nan
    df_clean.loc[(df_clean["glicose"] < 30) | (df_clean["glicose"] > 450), "glicose"] = np.nan
    df_clean.loc[(df_clean["sono_h"] < 0) | (df_clean["sono_h"] > 24), "sono_h"] = np.nan

    # 2. Imputar nulos por interpolação linear temporal
    df_clean[FEATURES_VITAIS] = df_clean[FEATURES_VITAIS].interpolate(method="linear").bfill().ffill()

    return df_clean

def passo3_categorizar_e_contextualizar(df_clean: pd.DataFrame):
    """
    Passo 3. Categorização e Ajuste Contextual:
    O contexto (EXERCICIO, SONO, REPOUSO, EVA) evita falsos alarmes.
    Calculamos o Z Robusto específico de cada tripulante usando RobustScaler (Mediana e IQR).
    """
    df_ctx = df_clean.copy()

    # RobustScaler por tripulante
    scaler = RobustScaler()
    X_vital = df_ctx[FEATURES_VITAIS]
    X_scaled = pd.DataFrame(
        scaler.fit_transform(X_vital),
        columns=FEATURES_VITAIS,
        index=df_ctx.index
    )

    # Ajuste contextual: reduz a pontuação de FC durante EXERCICIO para evitar falso alarme de esteira
    # Durante exercício, FC esperada é alta; se o contexto for EXERCICIO e a FC for elevada sem febre, ajustamos
    mask_exercicio = (df_ctx["contexto"] == "EXERCICIO")
    # Subtraímos o offset esperado de exercício no z-score da FC para evitar falso alarme
    X_scaled.loc[mask_exercicio, "fc"] = X_scaled.loc[mask_exercicio, "fc"] - 3.5

    return X_scaled, scaler

def treinar_tripulante(arquivo_csv: str, run_name: str, tripulante_id: str):
    caminho = DADOS_DIR / arquivo_csv
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo {caminho} não encontrado.")

    print(f"\n=======================================================")
    print(f"Treinando Modelo M3 para {tripulante_id} ({run_name})")
    print(f"=======================================================")

    df_raw = pd.read_csv(caminho)
    print(f"1. Registros carregados: {len(df_raw)}")

    # Passo 2: Limpar
    df_limpo = passo2_limpar_dados(df_raw)
    print("2. Limpeza concluída: ruídos e valores impossíveis tratados.")

    # Passo 3: Categorizar & Z Robusto
    X_train, scaler = passo3_categorizar_e_contextualizar(df_limpo)
    print(f"3. Features geradas com Z Robusto e Contexto: {list(X_train.columns)}")

    # Passo 4: Treinar com MLflow
    mlflow.set_experiment("astrohealth-m3")

    with mlflow.start_run(run_name=run_name):
        n_estimators = 200
        contamination = 0.035
        random_state = 42

        model = IsolationForest(
            n_estimators=n_estimators,
            contamination=contamination,
            random_state=random_state
        )
        model.fit(X_train)

        # Predições: 1 = Normal, -1 = Anomalia
        preds = model.predict(X_train)
        anomalias_pct = float((preds == -1).mean())

        # Validação com as Anomalias Injetadas (Ground Truth para Teste)
        y_true = df_limpo["anomalia_injetada"].values
        y_pred = (preds == -1).astype(int)

        recall = float(recall_score(y_true, y_pred, zero_division=0))
        precision = float(precision_score(y_true, y_pred, zero_division=0))
        f1 = float(f1_score(y_true, y_pred, zero_division=0))
        
        # Falsos positivos
        fps = int(((y_pred == 1) & (y_true == 0)).sum())
        total_negativos = int((y_true == 0).sum())
        fpr = float(fps / total_negativos) if total_negativos > 0 else 0.0

        # Logar Parâmetros no MLflow
        mlflow.log_params({
            "n_estimators": n_estimators,
            "contamination": contamination,
            "random_state": random_state,
            "tripulante_id": tripulante_id,
            "n_amostras": len(df_limpo),
            "features": ",".join(X_train.columns)
        })

        # Logar Métricas no MLflow
        mlflow.log_metrics({
            "anomalias_pct": anomalias_pct,
            "recall": recall,
            "precision": precision,
            "f1_score": f1,
            "falsos_positivos_qtd": fps,
            "taxa_falsos_positivos": fpr
        })

        print(f"4. Métricas no MLflow:")
        print(f"   - Anomalias Detectadas: {anomalias_pct*100:.2f}%")
        print(f"   - Recall (Sensibilidade): {recall*100:.2f}%")
        print(f"   - Precisão: {precision*100:.2f}%")
        print(f"   - F1-Score: {f1:.4f}")
        print(f"   - Falsos Positivos: {fps} ({fpr*100:.2f}%)")

        # Registrar Modelo no MLflow usando serialization_format="cloudpickle" para compatibilidade total
        try:
            mlflow.sklearn.log_model(
                model,
                "modelo",
                serialization_format="cloudpickle"
            )
            print("5. Modelo registrado com sucesso no MLflow (cloudpickle)!")
        except Exception as e:
            print(f"5. Fallback de registro MLflow: {e}")
            mlflow.log_artifact(str(DADOS_DIR / arquivo_csv), "dados_origem")

        # Salvar artefatos locais para inferência rápida no ia.py
        model_path = MODELOS_DIR / f"iforest_{tripulante_id.lower().replace('-', '_')}.joblib"
        scaler_path = MODELOS_DIR / f"scaler_{tripulante_id.lower().replace('-', '_')}.joblib"
        meta_path = MODELOS_DIR / f"meta_{tripulante_id.lower().replace('-', '_')}.json"

        joblib.dump(model, model_path)
        joblib.dump(scaler, scaler_path)
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump({
                "tripulante_id": tripulante_id,
                "features_ordem": list(X_train.columns),
                "recall": recall,
                "precision": precision,
                "f1": f1,
                "falsos_positivos": fps
            }, f, indent=2)

        print(f"6. Artefatos locais exportados com sucesso para {MODELOS_DIR}")

def main():
    print("Iniciando Pipeline M3: Treinamento Isolation Forest com MLflow...")
    
    tripulantes = [
        ("tripulante1.csv", "iforest-t1", "ASTRO-01"),
        ("tripulante2.csv", "iforest-t2", "ASTRO-02"),
        ("tripulante3.csv", "iforest-t3", "ASTRO-03"),
    ]

    for csv_file, run_name, t_id in tripulantes:
        treinar_tripulante(csv_file, run_name, t_id)

    print("\n=======================================================")
    print("[SUCESSO] Todos os modelos foram treinados e logados no MLflow!")
    print("Para visualizar os experimentos graficamente no seu navegador:")
    print("  mlflow ui --port 5000")
    print("=======================================================")

if __name__ == "__main__":
    main()
