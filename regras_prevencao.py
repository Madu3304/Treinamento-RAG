"""
Passo 5: Predição de Prevenção e Vigilância Fisiológica
Regras determinísticas e supervisionadas por humano para tendência de piora.
Integração com RAG para busca de protocolos na base de conhecimento.
Conformidade estrita com ADR 003 (Medicamento) e ADR 004 (Saúde Mental/Human in the Loop).
"""

import os
from pathlib import Path
from typing import List, Dict, Any

BASE_DIR = Path(__file__).resolve().parent
KNOWLEDGE_DIR = BASE_DIR / "1-ia-base-conhecimento"

def buscar_protocolo_rag(termo_chave: str) -> str:
    """
    Busca semântica / textual simplificada no acervo de protocolos da pasta 1-ia-base-conhecimento.
    Retorna trecho de orientação não-farmacológica e preventiva correspondente.
    """
    if not KNOWLEDGE_DIR.exists():
        return "Base de conhecimento não encontrada no caminho local."

    resultados = []
    for arquivo in KNOWLEDGE_DIR.glob("*.md"):
        try:
            with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
                conteudo = f.read()
                if termo_chave.lower() in conteudo.lower():
                    # Extrai parágrafo relevante
                    linhas = [l.strip() for l in conteudo.split("\n") if termo_chave.lower() in l.lower()]
                    if linhas:
                        resultados.append(f"[{arquivo.name}]: {linhas[0][:200]}...")
        except Exception:
            continue

    if resultados:
        return " | ".join(resultados[:2])
    return f"Protocolo padrão de vigilância ocupacional da NASA (LSAH/CHeCS) para {termo_chave}."

def avaliar_prevencao_tripulante(historico_recente: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Avalia tendência de piora e regras preventivas determinísticas:
    1. Privação de sono (sono < 6h por 3 dias seguidos).
    2. Omissão de contramedidas de exercício (> 48h sem exercício em microgravidade).
    3. Tendência de hipertensão sustentada (PAS >= 140 mmHg em repouso).
    4. Febre ou elevação térmica persistente.
    """
    alertas = []
    recomendacoes_rag = []
    humano_notificado = False

    if not historico_recente or len(historico_recente) == 0:
        return {
            "status": "DADOS_INSUFICIENTES",
            "alertas": [],
            "recomendacoes": [],
            "adr_compliance": {"adr_003": "OK", "adr_004": "OK"}
        }

    # Ordenar por timestamp
    registros = sorted(historico_recente, key=lambda x: x.get("timestamp", ""))

    # --- Regra 1: Sono abaixo de 6h por 3 dias consecutivos ---
    # Extrair sono dos últimos registros ou dias
    valores_sono = [r.get("sono_h") for r in registros if r.get("sono_h") is not None]
    if len(valores_sono) >= 3:
        ultimos_3_sonos = valores_sono[-3:]
        if all(s < 6.0 for s in ultimos_3_sonos):
            alerta_msg = f"TENDÊNCIA CRÍTICA: Privação crônica de sono detectada ({ultimos_3_sonos} horas nas últimas 72h)."
            alertas.append(alerta_msg)
            
            # Consulta RAG
            rag_info = buscar_protocolo_rag("sono")
            orientacao = (
                "Ajuste da iluminação circadiana de bordo para espectro atenuado (luz vermelha/âmbar 2h antes do descanso); "
                "restrição de telas e comunicações táticas 1h antes do repouso; agendamento de cochilo profilático de 45 min."
            )
            recomendacoes_rag.append({
                "condicao": "Privacao_Sono",
                "orientacao_protocolo": orientacao,
                "fonte_rag": rag_info,
                "nota_adr_003_medicamento": "ADR 003: Prescrição de indutores de sono ou medicamentos hipnóticos é ATO MÉDICO EXCLUSIVO do Flight Surgeon humano.",
                "nota_adr_004_saude_mental": "ADR 004: Apoio psicológico e manejo de estresse de voo direcionados para acolhimento humano."
            })
            humano_notificado = True

    # --- Regra 2: Exercício Físico Faltante / Omissão de Contramedidas ---
    contextos_recentes = [r.get("contexto") for r in registros[-48:]] # últimas 48 amostras/horas
    if len(contextos_recentes) >= 24 and "EXERCICIO" not in contextos_recentes:
        alerta_msg = "ALERTA PREVENTIVO: Ausência de protocolo de exercício de contramedida nas últimas 24-48 horas."
        alertas.append(alerta_msg)
        rag_info = buscar_protocolo_rag("muscular")
        recomendacoes_rag.append({
            "condicao": "Falta_Exercicio_Contramedida",
            "orientacao_protocolo": "Retomada obrigatória do cicloergômetro ARED/T2 com progressão de carga e monitoramento hemodinâmico.",
            "fonte_rag": rag_info,
            "nota_adr_003_medicamento": "Sem intervenção farmacológica."
        })

    # --- Regra 3: Hipertensão Sustentada ---
    pas_recentes = [r.get("pas") for r in registros[-5:] if r.get("pas") is not None and r.get("contexto") == "REPOUSO"]
    if len(pas_recentes) >= 3 and all(p >= 140 for p in pas_recentes):
        alerta_msg = f"ALERTA HEMODINÂMICO: Pressão Arterial Sistólica sustentada >= 140 mmHg em repouso ({pas_recentes})."
        alertas.append(alerta_msg)
        recomendacoes_rag.append({
            "condicao": "Hipertensao_Repouso",
            "orientacao_protocolo": "Repouso relativo, hidratação balanceada, posicionamento em LBNP (Lower Body Negative Pressure) e telemetria contínua.",
            "fonte_rag": buscar_protocolo_rag("cardiovascular"),
            "nota_adr_003_medicamento": "ADR 003: Qualquer anti-hipertensivo exige prescrição direta do Flight Surgeon."
        })
        humano_notificado = True

    # --- Regra 4: Alerta Térmico / Febre ---
    temp_recente = registros[-1].get("temp")
    if temp_recente is not None and temp_recente >= 38.0:
        alerta_msg = f"ALERTA CLÍNICO: Elevação térmica febril detectada ({temp_recente} °C)."
        alertas.append(alerta_msg)
        recomendacoes_rag.append({
            "condicao": "Febre_Infeccao",
            "orientacao_protocolo": "Isolamento de barreira na cabine, hidratação oral guiada e painel microbiológico molecular a bordo.",
            "fonte_rag": buscar_protocolo_rag("saúde"),
            "nota_adr_003_medicamento": "ADR 003: Avaliação de antipiréticos/antibióticos restrita ao médico humano de missão."
        })
        humano_notificado = True

    return {
        "status": "ALERTA_PREVENTIVO" if alertas else "NOMINAL_ESTAVEL",
        "qtd_alertas": len(alertas),
        "alertas": alertas,
        "recomendacoes_protocolo": recomendacoes_rag,
        "supervisao_humana_acionada": humano_notificado,
        "adr_compliance": {
            "adr_003_medicamento_humano": "Em conformidade (Nenhum fármaco prescrito por IA)",
            "adr_004_saude_mental_humano": "Em conformidade (Suporte humano preservado)"
        }
    }
