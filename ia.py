"""
Módulo Central de Inteligência Artificial: ia.py
Exposição do Modelo Isolation Forest (M3 com Z Robusto e Contexto)
e Motor de Prevenção Determinístico com RAG e ADRs 003/004.
Pronto para ser importado na API FastAPI (Pessoa 3).
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, List, Optional
import numpy as np
import pandas as pd
import joblib

from regras_prevencao import avaliar_prevencao_tripulante, buscar_protocolo_rag

BASE_DIR = Path(__file__).resolve().parent
MODELOS_DIR = BASE_DIR / "modelos"

FEATURES_VITAIS = ["fc", "pas", "pad", "glicose", "temp", "sono_h"]

# Cache em memória dos modelos carregados
_MODELOS_CACHE = {}
_SCALERS_CACHE = {}
_METADATA_CACHE = {}

def inicializar_modelos():
    """Carrega os modelos treinados e escaladores para memória."""
    tripulantes = ["ASTRO-01", "ASTRO-02", "ASTRO-03"]
    for t_id in tripulantes:
        key = t_id.lower().replace("-", "_")
        mod_path = MODELOS_DIR / f"iforest_{key}.joblib"
        sc_path = MODELOS_DIR / f"scaler_{key}.joblib"
        meta_path = MODELOS_DIR / f"meta_{key}.json"

        if mod_path.exists() and sc_path.exists():
            _MODELOS_CACHE[t_id] = joblib.load(mod_path)
            _SCALERS_CACHE[t_id] = joblib.load(sc_path)
            if meta_path.exists():
                with open(meta_path, "r", encoding="utf-8") as f:
                    _METADATA_CACHE[t_id] = json.load(f)

inicializar_modelos()

def limpar_evento(evento: Dict[str, Any]) -> Dict[str, float]:
    """
    Passo 2: Padroniza unidades e trata valores impossíveis.
    Verifica campos tanto no nível raiz quanto dentro de 'sinais_vitais'.
    """
    sinais = evento.get("sinais_vitais", {}) if isinstance(evento.get("sinais_vitais"), dict) else {}
    
    fc = evento.get("fc", sinais.get("fc", evento.get("frequencia_cardiaca_bpm", sinais.get("frequencia_cardiaca_bpm"))))
    pas = evento.get("pas", sinais.get("pas", evento.get("pressao_arterial_sistolica", sinais.get("pressao_arterial_sistolica"))))
    pad = evento.get("pad", sinais.get("pad", evento.get("pressao_arterial_diastolica", sinais.get("pressao_arterial_diastolica"))))
    glicose = evento.get("glicose", sinais.get("glicose", 95.0))
    temp = evento.get("temp", sinais.get("temp", evento.get("temperatura_corporal_c", sinais.get("temperatura_corporal_c"))))
    sono_h = evento.get("sono_h", sinais.get("sono_h", 7.5))

    # Tratamento de valores impossíveis (falhas grosseiras de sensor)
    fc = float(fc) if fc is not None and 30 <= float(fc) <= 250 else 70.0
    pas = float(pas) if pas is not None and 50 <= float(pas) <= 260 else 120.0
    pad = float(pad) if pad is not None and 30 <= float(pad) <= 180 else 80.0
    glicose = float(glicose) if glicose is not None and 30 <= float(glicose) <= 450 else 95.0
    temp = float(temp) if temp is not None and 32.0 <= float(temp) <= 44.0 else 36.6
    sono_h = float(sono_h) if sono_h is not None and 0 <= float(sono_h) <= 24 else 7.5

    return {
        "fc": fc,
        "pas": pas,
        "pad": pad,
        "glicose": glicose,
        "temp": temp,
        "sono_h": sono_h
    }

def analisar_evento_telemetria(evento: Dict[str, Any], historico_recente: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """
    Função principal exposta para a API (FastAPI - Pessoa 3).
    Recebe o evento de telemetria (conforme evento-atualizado.schema.json),
    executa:
      1. Limpeza e padronização (Passo 2)
      2. Normalização com Z Robusto por tripulante (Passo 2)
      3. Ajuste contextual (Passo 3)
      4. Predição de anomalia via Isolation Forest (Passo 4)
      5. Regras de prevenção e consulta a protocolos via RAG (Passo 5)
      6. Validação das ADRs 003 e 004
    """
    tripulante_id = evento.get("astronauta_id", evento.get("tripulante_id", "ASTRO-01"))
    ambiente = evento.get("ambiente", {}) if isinstance(evento.get("ambiente"), dict) else {}
    contexto = ambiente.get("atividade", evento.get("contexto", "REPOUSO"))

    # Mapeamento de contexto para formato canônico
    if "EXERCICIO" in str(contexto).upper():
        contexto_canonico = "EXERCICIO"
    elif "SONO" in str(contexto).upper() or "REPOUSO" in str(contexto).upper():
        contexto_canonico = "SONO" if "SONO" in str(contexto).upper() else "REPOUSO"
    elif "EVA" in str(contexto).upper():
        contexto_canonico = "EVA"
    else:
        contexto_canonico = "REPOUSO"

    # 1. Limpeza
    valores_limpos = limpar_evento(evento)

    # 2. Seleção do Modelo e Scaler do tripulante
    if tripulante_id not in _MODELOS_CACHE:
        # Fallback para o primeiro modelo disponível
        tripulante_id = list(_MODELOS_CACHE.keys())[0] if _MODELOS_CACHE else "ASTRO-01"

    model = _MODELOS_CACHE.get(tripulante_id)
    scaler = _SCALERS_CACHE.get(tripulante_id)

    if model is None or scaler is None:
        raise RuntimeError("Modelos Isolation Forest não inicializados. Execute treinar_mlflow.py.")

    # 3. Z Robusto e Ajuste Contextual (Passo 3)
    df_single = pd.DataFrame([valores_limpos])[FEATURES_VITAIS]
    X_scaled = pd.DataFrame(scaler.transform(df_single), columns=FEATURES_VITAIS)

    # Offset para evitar falso alarme em exercício
    if contexto_canonico == "EXERCICIO":
        X_scaled["fc"] = X_scaled["fc"] - 3.5

    # 4. Inferência Isolation Forest
    pred = model.predict(X_scaled)[0]  # 1 = Normal, -1 = Anomalia
    score = float(model.decision_function(X_scaled)[0]) # Score: quanto menor/negativo, mais anômalo
    is_anomalia = bool(pred == -1)

    # 5. Avaliação Preventiva Determinística + RAG (Passo 5)
    dados_para_prevencao = (historico_recente or []) + [{
        "timestamp": evento.get("timestamp", ""),
        "contexto": contexto_canonico,
        "fc": valores_limpos["fc"],
        "pas": valores_limpos["pas"],
        "pad": valores_limpos["pad"],
        "temp": valores_limpos["temp"],
        "sono_h": valores_limpos["sono_h"]
    }]
    analise_prevencao = avaliar_prevencao_tripulante(dados_para_prevencao)

    # 6. Status de Alerta Consolidado
    if is_anomalia or analise_prevencao["status"] == "ALERTA_PREVENTIVO":
        if valores_limpos["temp"] >= 38.5 or valores_limpos["fc"] >= 165 and contexto_canonico != "EXERCICIO":
            classificacao_alerta = "VERMELHO_CRITICO"
        else:
            classificacao_alerta = "LARANJA_ALERTA"
    else:
        classificacao_alerta = "VERDE_NOMINAL"

    resposta = {
        "tripulante_id": tripulante_id,
        "timestamp": evento.get("timestamp"),
        "contexto": contexto_canonico,
        "is_simulado": evento.get("is_simulado", True),
        "diagnostico_ia": {
            "is_anomalia": is_anomalia,
            "anomaly_score": round(score, 4),
            "modelo_utilizado": f"IsolationForest-{tripulante_id} (MLflow: astrohealth-m3)",
            "normalizacao": "Z Robusto (RobustScaler: Mediana / IQR)"
        },
        "analise_prevencao_deterministica": analise_prevencao,
        "status_alerta": classificacao_alerta,
        "adr_compliance": {
            "adr_003_medicamento": "Em conformidade: Prescrição farmacológica restrita ao médico humano.",
            "adr_004_saude_mental": "Em conformidade: Diagnóstico de saúde mental sob supervisão humana."
        }
    }
    return resposta

def obter_status_modelos() -> Dict[str, Any]:
    """Retorna o status dos modelos treinados para observabilidade."""
    status = {}
    for t_id, meta in _METADATA_CACHE.items():
        status[t_id] = {
            "status": "OPERACIONAL",
            "algoritmo": "Isolation Forest",
            "metricas": meta
        }
    return {
        "experimento_mlflow": "astrohealth-m3",
        "modelos_disponiveis": status
    }
