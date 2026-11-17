"""
Passo 1: Capturar / Gerar Datasets Sintéticos Realistas de Saúde dos Astronautas
Conforme evento-atualizado.schema.json e dados públicos de apoio (PhysioNet CinC 2017, NASA LSDA).

IMPORTANTE (Pitch & Ética):
Dados médicos reais de astronautas são estritamente confidenciais, raros e restritos
(HIPAA / NASA IRB). Os dados individuais de séries temporais aqui gerados são 100%
sintéticos e simulados com alta fidelidade fisiológica.
"""

import os
import json
from pathlib import Path
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

BASE_DIR = Path(__file__).resolve().parent
DADOS_DIR = BASE_DIR / "dados"
DADOS_DIR.mkdir(parents=True, exist_ok=True)

np.random.seed(42)

def gerar_historico_tripulante(tripulante_id: str, nome: str, dias=30, freq_minutos=60):
    """
    Gera histórico temporal de sinais vitais e telemetria para um tripulante,
    respeitando o ciclo circadiano, fase da missão e contextos de atividade.
    """
    inicio = datetime(2026, 10, 1, 0, 0, 0)
    total_pontos = (dias * 24 * 60) // freq_minutos
    timestamps = [inicio + timedelta(minutes=i * freq_minutos) for i in range(total_pontos)]

    registros = []
    
    # Baseline individual do tripulante (M3 individualizado)
    baseline_fc = np.random.uniform(62, 70)
    baseline_pas = np.random.uniform(114, 122)
    baseline_pad = np.random.uniform(72, 78)
    baseline_temp = np.random.uniform(36.5, 36.7)
    baseline_glicose = np.random.uniform(92, 98)
    sono_diario_atual = 7.5

    for idx, ts in enumerate(timestamps):
        hora = ts.hour
        dia_missao = (ts - inicio).days

        # Determinar Fase da Missão
        if dia_missao < 5:
            fase = "ORBITA_ISS"
        elif dia_missao < 18:
            fase = "TRANSITO_LUNAR"
        else:
            fase = "SUPERFICIE_LUNAR"

        # Determinar Contexto pelo ciclo diário de rotina de bordo
        if 23 <= hora or hora < 7:
            contexto = "SONO"
        elif 9 <= hora < 11:
            contexto = "EXERCICIO"  # Protocolo obrigatório de contramedida NASA (esteira ARED/T2)
        elif 14 <= hora < 18 and dia_missao in [19, 21, 24, 26]:
            contexto = "EVA"        # Atividade Extraveicular
        else:
            contexto = "REPOUSO"

        # Variabilidade fisiológica de acordo com o contexto
        if contexto == "SONO":
            fc = np.random.normal(baseline_fc - 12, 3.0)
            pas = np.random.normal(baseline_pas - 8, 3.5)
            pad = np.random.normal(baseline_pad - 6, 2.5)
            temp = np.random.normal(baseline_temp - 0.4, 0.15)
            glicose = np.random.normal(baseline_glicose - 5, 4.0)
            spo2 = np.random.normal(98.5, 0.5)
        elif contexto == "EXERCICIO":
            # Em exercício a FC sobe significativamente sem ser anomalia patológica
            fc = np.random.normal(148, 10.0)
            pas = np.random.normal(baseline_pas + 25, 8.0)
            pad = np.random.normal(baseline_pad + 5, 4.0)
            temp = np.random.normal(baseline_temp + 0.6, 0.25)
            glicose = np.random.normal(baseline_glicose + 15, 6.0)
            spo2 = np.random.normal(97.8, 0.6)
        elif contexto == "EVA":
            fc = np.random.normal(baseline_fc + 25, 6.0)
            pas = np.random.normal(baseline_pas + 12, 5.0)
            pad = np.random.normal(baseline_pad + 6, 3.0)
            temp = np.random.normal(baseline_temp + 0.2, 0.2)
            glicose = np.random.normal(baseline_glicose + 8, 5.0)
            spo2 = np.random.normal(98.0, 0.5)
        else:  # REPOUSO
            fc = np.random.normal(baseline_fc, 4.0)
            pas = np.random.normal(baseline_pas, 4.0)
            pad = np.random.normal(baseline_pad, 3.0)
            temp = np.random.normal(baseline_temp, 0.15)
            glicose = np.random.normal(baseline_glicose, 5.0)
            spo2 = np.random.normal(98.8, 0.4)

        # Atualização do registro diário de horas de sono
        if hora == 7:
            sono_diario_atual = float(np.clip(np.random.normal(7.2, 0.8), 4.5, 9.5))
        sono_h = sono_diario_atual

        anomalia_injetada = 0
        tipo_anomalia = "NORMAL"

        # --- Injeção de Anomalias Fisiológicas para Validação Supervisionada ---
        # 1. Arritmia / Taquicardia durante SONO (inspirado no PhysioNet CinC 2017)
        if dia_missao == 10 and 2 <= hora <= 4:
            fc += 65.0  # Taquicardia paroxística súbita em pleno repouso/sono
            pas += 28.0
            anomalia_injetada = 1
            tipo_anomalia = "ARRITMIA_EM_SONO"

        # 2. Febre e resposta inflamatória súbita
        elif dia_missao == 15 and 11 <= hora <= 18:
            temp += 2.2  # Febre > 38.8 °C
            fc += 35.0
            anomalia_injetada = 1
            tipo_anomalia = "FEBRE_INFECCAO"

        # 3. Privação Crônica de Sono (3 dias seguidos com < 5.0h)
        elif dia_missao in [22, 23, 24]:
            sono_h = 4.2
            pas += 16.0  # Estresse hemodinâmico secundário
            if dia_missao == 24 and hora >= 12:
                anomalia_injetada = 1
                tipo_anomalia = "PRIVACAO_CRONICA_SONO"

        # 4. Hipóxia e dessaturação súbita durante EVA
        elif dia_missao == 26 and contexto == "EVA" and 15 <= hora <= 16:
            spo2 -= 11.0  # Dessaturação < 88%
            fc += 40.0
            anomalia_injetada = 1
            tipo_anomalia = "HIPOXIA_EVA"

        # --- Injeção de Ruídos de Sensor / Valores Impossíveis para o Passo 2 Limpar ---
        # Artefatos conhecidos de medição em vestíveis aeroespaciais
        if idx == 45:
            fc = 0.0          # Sensor desconectou momentaneamente (valor impossível)
        elif idx == 112:
            temp = 80.0       # Spike térmico elétrico do termopar (impossível)
        elif idx == 180:
            pas = None        # Falha transitória de telemetria
        elif idx == 181:
            pad = None

        registros.append({
            "timestamp": ts.isoformat() + "Z",
            "tripulante_id": tripulante_id,
            "nome": nome,
            "fase_missao": fase,
            "contexto": contexto,
            "fc": round(fc, 1) if fc is not None else None,
            "pas": round(pas, 1) if pas is not None else None,
            "pad": round(pad, 1) if pad is not None else None,
            "glicose": round(glicose, 1) if glicose is not None else None,
            "temp": round(temp, 2) if temp is not None else None,
            "sono_h": round(sono_h, 2) if sono_h is not None else None,
            "spo2": round(spo2, 1) if spo2 is not None else None,
            "anomalia_injetada": anomalia_injetada,
            "tipo_anomalia": tipo_anomalia
        })

    df = pd.DataFrame(registros)
    return df

def main():
    print("=== Passo 1: Captura e Geração de Datasets de Saúde dos Astronautas ===")
    print("[Nota Ética/Pitch]: Dados simulados gerados para treinamento e validação do M3.")
    
    tripulantes = [
        ("ASTRO-01", "Comandante Silva", "tripulante1.csv"),
        ("ASTRO-02", "Dra. Santos (Med)", "tripulante2.csv"),
        ("ASTRO-03", "Engenheiro Tanaka", "tripulante3.csv"),
    ]

    todos_dfs = []
    for t_id, nome, arquivo in tripulantes:
        print(f"Gerando histórico fisiológico para {t_id} ({nome})...")
        df_trip = gerar_historico_tripulante(t_id, nome, dias=30, freq_minutos=60)
        caminho_csv = DADOS_DIR / arquivo
        df_trip.to_csv(caminho_csv, index=False, encoding="utf-8")
        print(f"  -> Salvo: {caminho_csv} ({len(df_trip)} registros)")
        todos_dfs.append(df_trip)

    df_consolidado = pd.concat(todos_dfs, ignore_index=True)
    caminho_consolidado = DADOS_DIR / "historico_saude_processos.csv"
    df_consolidado.to_csv(caminho_consolidado, index=False, encoding="utf-8")
    print(f"\n[Sucesso] Dataset consolidado salvo em: {caminho_consolidado} ({len(df_consolidado)} registros)")

if __name__ == "__main__":
    main()
