"""
Módulo de Gamificação: Bioma Cooperativo & Elo Terra-Espaço
Lógica de dados pura (sem treino de modelo de machine learning).

1. Bioma Cooperativo:
   Agregação coletiva das métricas de adesão de bem-estar da tripulação:
   - Hidratação (ingestão de água vs. meta de 2.500 mL)
   - Sono (horas dormidas vs. meta de 7 a 8 horas)
   - Exercício (contramedida física na esteira/ARED vs. meta de 60 min)
   Gera o Índice de Vitalidade do Bioma (0 a 100%) e status ecológico compartilhado.

2. Elo Terra-Espaço:
   Conexão afetiva e colaborativa entre astronauta e seu familiar na Terra:
   - Respeito estrito ao Consentimento Informado (LGPD / HIPAA / NASA Privacy):
     Apenas métricas de hábitos autorizadas são compartilhadas. Dados clínicos,
     sinais vitais brutos e diagnósticos médicos são ESTRITAMENTE PRIVADOS.
   - Metas compartilhadas (ex.: passos/km na esteira da ISS + caminhada na Terra).
   - Mensagens de apoio e badges de conquista sincronizados.
"""

from datetime import datetime
from typing import Dict, List, Any, Optional

# --- 1. BIOMA COOPERATIVO ---

METAS_NOMINAIS = {
    "hidratacao_ml": 2500.0,  # 2.5 L/dia em microgravidade
    "sono_h": 7.5,            # 7.5 horas de sono
    "exercicio_min": 60.0     # 60 minutos de exercício físico diário
}

PESOS_METRICAS = {
    "hidratacao": 0.30,
    "sono": 0.35,
    "exercicio": 0.35
}

def calcular_adesao_individual(registro_astronauta: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calcula a adesão de um astronauta individual aos pilares de saúde do dia:
    - Ingestão hídrica
    - Duração do sono
    - Minutos de contramedida de exercício físico
    """
    t_id = registro_astronauta.get("astronauta_id", "DESCONHECIDO")
    nome = registro_astronauta.get("nome", t_id)

    hid_ml = float(registro_astronauta.get("hidratacao_ml", 0.0))
    sono_h = float(registro_astronauta.get("sono_h", 0.0))
    exe_min = float(registro_astronauta.get("exercicio_min", 0.0))

    # Índices parciais de adesão (limitados a 100% para não distorcer)
    adesao_hid = min(1.0, hid_ml / METAS_NOMINAIS["hidratacao_ml"]) if METAS_NOMINAIS["hidratacao_ml"] > 0 else 0.0
    adesao_sono = min(1.0, sono_h / METAS_NOMINAIS["sono_h"]) if METAS_NOMINAIS["sono_h"] > 0 else 0.0
    adesao_exe = min(1.0, exe_min / METAS_NOMINAIS["exercicio_min"]) if METAS_NOMINAIS["exercicio_min"] > 0 else 0.0

    score_individual = (
        adesao_hid * PESOS_METRICAS["hidratacao"] +
        adesao_sono * PESOS_METRICAS["sono"] +
        adesao_exe * PESOS_METRICAS["exercicio"]
    ) * 100.0

    return {
        "astronauta_id": t_id,
        "nome": nome,
        "score_vitalidade_individual": round(score_individual, 1),
        "detalhes_adesao": {
            "hidratacao": {
                "realizado_ml": hid_ml,
                "meta_ml": METAS_NOMINAIS["hidratacao_ml"],
                "adesao_pct": round(adesao_hid * 100, 1)
            },
            "sono": {
                "realizado_h": sono_h,
                "meta_h": METAS_NOMINAIS["sono_h"],
                "adesao_pct": round(adesao_sono * 100, 1)
            },
            "exercicio": {
                "realizado_min": exe_min,
                "meta_min": METAS_NOMINAIS["exercicio_min"],
                "adesao_pct": round(adesao_exe * 100, 1)
            }
        }
    }

def calcular_bioma_cooperativo(tripulacao_registros: List[Dict[str, Any]], dias_consecutivos_sucesso: int = 1) -> Dict[str, Any]:
    """
    Agrega as métricas de adesão de toda a tripulação em um Índice Coletivo do Bioma.
    Simula um ecossistema vivo na espaçonave que floresce com a cooperação de todos.
    """
    if not tripulacao_registros:
        return {
            "status": "SEM_DADOS",
            "indice_bioma_pct": 0.0,
            "estado_ecologico": "Bioma Inativo"
        }

    avaliacoes_individuais = [calcular_adesao_individual(reg) for reg in tripulacao_registros]
    scores = [a["score_vitalidade_individual"] for a in avaliacoes_individuais]
    
    media_coletiva = sum(scores) / len(scores)

    # Multiplicador cooperativo por dias consecutivos (streak de hábitos coletivos)
    bonus_streak = min(5.0, (dias_consecutivos_sucesso - 1) * 1.0) if media_coletiva >= 70.0 else 0.0
    indice_final = min(100.0, round(media_coletiva + bonus_streak, 1))

    # Classificação do estado ecológico do Bioma
    if indice_final >= 90.0:
        estado = "Bioma Florescente 🌿🌸"
        descricao = "Ecossistema em ápice de vigor. Flora orbital exuberante e oxigenação ótima."
        recompensa_coletiva = "Badge Conquistado: Guardiões da Biosfera Nível Ouro ✨"
    elif indice_final >= 75.0:
        estado = "Bioma Estável 🍃"
        descricao = "Equilíbrio sustentável mantido. Hábitos consistentes entre os tripulantes."
        recompensa_coletiva = "Badge Conquistado: Harmonia Orbital Nível Prata 🛡️"
    elif indice_final >= 55.0:
        estado = "Bioma em Atenção 🍂"
        descricao = "Folhagem perdendo turgor. Déficit em hidratação ou descanso identificado."
        recompensa_coletiva = "Missão de Resgate: Hidratação em grupo necessária para restaurar o ciclo."
    else:
        estado = "Bioma Ressecado / Crítico ⚠️"
        descricao = "Sinais de estresse sistêmico coletivo. Rotinas de sono e contramedidas negligenciadas."
        recompensa_coletiva = "Ação Imediata: Pausa operacional para regeneração coletiva."

    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "tripulantes_avaliados": len(tripulacao_registros),
        "indice_bioma_coletivo_pct": indice_final,
        "bonus_cooperativo_streak": round(bonus_streak, 1),
        "estado_ecologico": estado,
        "descricao_narrativa": descricao,
        "recompensa_coletiva": recompensa_coletiva,
        "desempenho_por_tripulante": avaliacoes_individuais
    }


# --- 2. ELO TERRA-ESPAÇO ---

def filtrar_dados_com_consentimento(dados_astronauta: Dict[str, Any], termo_consentimento: Dict[str, bool]) -> Dict[str, Any]:
    """
    Filtro estrito de Privacidade e Consentimento (Privacy by Design).
    Garante que APENAS métricas de estilo de vida expressamente autorizadas
    sejam transmitidas para a família. Dados médicos, patologias ou sinais vitais
    clínicos nunca são expostos.
    """
    dados_compartilhaveis = {
        "astronauta_id": dados_astronauta.get("astronauta_id"),
        "nome": dados_astronauta.get("nome"),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    # Só compartilha se houver consentimento explícito booleano True
    if termo_consentimento.get("compartilhar_exercicio", False):
        dados_compartilhaveis["exercicio_min"] = dados_astronauta.get("exercicio_min", 0.0)
        dados_compartilhaveis["km_esteira_ou_ciclo"] = round(dados_astronauta.get("exercicio_min", 0.0) * 0.15, 2)

    if termo_consentimento.get("compartilhar_hidratacao", False):
        dados_compartilhaveis["copos_agua"] = int(dados_astronauta.get("hidratacao_ml", 0.0) // 250)

    if termo_consentimento.get("compartilhar_sono_horas", False):
        dados_compartilhaveis["horas_sono"] = dados_astronauta.get("sono_h", 0.0)

    # Proteção de dados clínicos (nunca compartilha)
    campos_bloqueados = ["fc", "pas", "pad", "temp", "diagnostico", "anomalia", "ecg", "medicacao"]
    for campo in campos_bloqueados:
        if campo in dados_astronauta:
            # Nunca inclui no retorno
            pass

    return dados_compartilhaveis

def sincronizar_meta_compartilhada_familia(
    dados_espaco: Dict[str, Any],
    dados_terra: Dict[str, Any],
    desafio_nome: str = "Corrida Terra-Lua Compartilhada"
) -> Dict[str, Any]:
    """
    Cruza as atividades do astronauta em órbita com as do familiar na Terra,
    promovendo conexão emocional através de um objetivo compartilhado.
    """
    km_espaco = float(dados_espaco.get("km_esteira_ou_ciclo", 0.0))
    km_terra = float(dados_terra.get("km_caminhada_ou_corrida", 0.0))
    km_total_dupla = km_espaco + km_terra

    meta_km_semanal = 50.0  # Meta conjunta semanal Terra-Espaço
    progresso_pct = min(100.0, round((km_total_dupla / meta_km_semanal) * 100, 1))

    # Mensagens de incentivo mútuo
    mensagens_terra = dados_terra.get("mensagens_recebidas", [])
    cartoes_incentivo = [
        f"Recado da Terra ({dados_terra.get('familiar_nome', 'Família')}): '{m}'" 
        for m in mensagens_terra
    ]

    badge = None
    if progresso_pct >= 100.0:
        badge = "🏆 Medalha de Órbita Cruzada: Conexão Terra-Espaço Completa!"
    elif progresso_pct >= 50.0:
        badge = "🚀 Insígnia Meio-Caminho Cósmico"

    return {
        "desafio": desafio_nome,
        "astronauta": dados_espaco.get("nome"),
        "familiar_terra": dados_terra.get("familiar_nome"),
        "parentesco": dados_terra.get("parentesco", "Familiar"),
        "contribuicao_espaco_km": km_espaco,
        "contribuicao_terra_km": km_terra,
        "km_combinado": round(km_total_dupla, 2),
        "meta_semanal_km": meta_km_semanal,
        "progresso_dupla_pct": progresso_pct,
        "badge_desbloqueado": badge,
        "cartoes_incentivo": cartoes_incentivo,
        "status_conexao": "SINCRONIZADO_EM_TEMPO_REAL"
    }

