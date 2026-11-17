import os
import json
import argparse
import numpy as np
import requests

OLLAMA_BASE_URL = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
EMBED_MODEL = "nomic-embed-text:latest"
CHAT_MODEL = "llama3.2:3b"

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(CURRENT_DIR, "astronauts_complete.json")
EMBEDDINGS_CACHE = os.path.join(CURRENT_DIR, "astronauts_embeddings.npz")

session = requests.Session()

def get_embedding(text: str) -> np.ndarray:
    url = f"{OLLAMA_BASE_URL}/api/embeddings"
    payload = {"model": EMBED_MODEL, "prompt": text}
    response = session.post(url, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()
    return np.array(data["embedding"], dtype=np.float32)

def format_astronaut_doc(item: dict) -> str:
    name = item.get("name") or "Desconhecido"
    nat = item.get("nationality") or "Não informada"
    birth = item.get("birth_date") or str(item.get("birth_year") or "N/D")
    death = item.get("death_date") or "N/D (Vivo/Não informado)"
    sex = item.get("sex") or "N/D"
    employers = item.get("employers") or "Não informado"
    flights = item.get("num_flights")
    flights_str = f"{flights}" if flights is not None else "N/D"
    hours = item.get("time_in_space_hours")
    mins = item.get("time_in_space_min")
    hours_str = f"{float(hours):.2f}" if hours is not None else "0.00"
    mins_str = f"{float(mins):.0f}" if mins is not None else "0"
    wiki = item.get("wikidata_id") or ""

    return (
        f"Astronauta: {name}\n"
        f"- Nacionalidade: {nat}\n"
        f"- Sexo: {sex}\n"
        f"- Data de Nascimento: {birth} | Falecimento: {death}\n"
        f"- Empregador(es): {employers}\n"
        f"- Quantidade de Voos Espaciais: {flights_str}\n"
        f"- Tempo total no espaço: {hours_str} horas ({mins_str} minutos)\n"
        f"- Wikidata ID: {wiki}"
    )

def prepare_documents():
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Arquivo de dados não encontrado: {DATA_FILE}. Execute fetch_dataset.py primeiro.")
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        astronauts = json.load(f)

    docs = []
    for item in astronauts:
        doc_text = format_astronaut_doc(item)
        docs.append({"raw": item, "text": doc_text, "name": item.get("name", "")})
    return docs

def build_or_load_vectorstore(docs):
    if os.path.exists(EMBEDDINGS_CACHE):
        print(f"Carregando embeddings em cache de: {EMBEDDINGS_CACHE}")
        npz = np.load(EMBEDDINGS_CACHE)
        embeddings = npz["embeddings"]
        if len(embeddings) == len(docs):
            return embeddings

    print(f"Gerando embeddings com Ollama ({EMBED_MODEL}) para {len(docs)} astronautas...")
    embeddings_list = []
    for idx, doc in enumerate(docs):
        emb = get_embedding(doc["text"])
        embeddings_list.append(emb)
        if (idx + 1) % 50 == 0 or idx == len(docs) - 1:
            print(f"Indexados: {idx + 1}/{len(docs)}...")

    embeddings = np.array(embeddings_list, dtype=np.float32)
    # Normalizar para cosine similarity
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    norms[norms == 0] = 1e-10
    normalized_embeddings = embeddings / norms

    np.savez_compressed(EMBEDDINGS_CACHE, embeddings=normalized_embeddings)
    print(f"Embeddings salvos em cache com sucesso: {EMBEDDINGS_CACHE}")
    return normalized_embeddings

def search_astronauts(query: str, docs, embeddings, top_k: int = 5):
    query_emb = get_embedding(query)
    q_norm = np.linalg.norm(query_emb)
    if q_norm > 0:
        query_emb = query_emb / q_norm

    # Cosine similarity
    dense_scores = np.dot(embeddings, query_emb)

    # Keyword booster para nomes exatos na query
    query_lower = query.lower()
    final_scores = np.copy(dense_scores)
    for i, doc in enumerate(docs):
        doc_name = (doc.get("name") or "").lower()
        if doc_name and doc_name in query_lower:
            final_scores[i] += 0.5

    top_indices = np.argsort(final_scores)[::-1][:top_k]

    results = []
    for idx in top_indices:
        results.append((docs[idx], float(final_scores[idx])))
    return results

def ask_ollama(prompt: str, system_prompt: str = None) -> str:
    url = f"{OLLAMA_BASE_URL}/api/generate"
    payload = {
        "model": CHAT_MODEL,
        "prompt": prompt,
        "stream": False
    }
    if system_prompt:
        payload["system"] = system_prompt

    res = session.post(url, json=payload, timeout=90)
    res.raise_for_status()
    return res.json()["response"]

def answer_query_rag(query: str, docs, embeddings, top_k: int = 5):
    print(f"\n[Consulta]: {query}")
    print("[RAG] Buscando astronautas mais relevantes...")
    retrieved = search_astronauts(query, docs, embeddings, top_k=top_k)

    context_blocks = []
    print("\n--- Documentos Recuperados ---")
    for doc, score in retrieved:
        print(f"* {doc['name']} (Score: {score:.4f})")
        context_blocks.append(doc["text"])
    print("------------------------------\n")

    context_str = "\n\n".join(context_blocks)
    system_prompt = (
        "Você é um assistente especialista em missões espaciais e na base de dados de astronautas. "
        "Responda à pergunta do usuário utilizando prioritariamente o contexto fornecido abaixo. "
        "Se a informação não estiver no contexto, seja honesto e informe com base nos seus conhecimentos. "
        "Responda em português de forma clara e objetiva."
    )
    user_prompt = f"Contexto de Astronautas:\n{context_str}\n\nPergunta do usuário: {query}\n\nResposta:"

    print(f"[Ollama] Gerando resposta com o modelo '{CHAT_MODEL}'...")
    response = ask_ollama(user_prompt, system_prompt)
    return response

def main():
    parser = argparse.ArgumentParser(description="RAG local com Ollama e Dataset de Astronautas Hugging Face")
    parser.add_argument("--query", "-q", type=str, help="Pergunta a ser respondida pelo RAG")
    parser.add_argument("--top-k", "-k", type=int, default=5, help="Quantidade de registros para recuperar")
    args = parser.parse_args()

    print("Inicializando Sistema RAG Astronautas com Ollama local...")
    docs = prepare_documents()
    embeddings = build_or_load_vectorstore(docs)

    if args.query:
        ans = answer_query_rag(args.query, docs, embeddings, top_k=args.top_k)
        print("\n=== RESPOSTA DO MODELO ===")
        print(ans)
    else:
        print("\n--- Modo Interativo RAG (digite 'sair' para encerrar) ---")
        while True:
            try:
                q = input("\nPergunta: ").strip()
                if not q or q.lower() in ["sair", "exit", "quit"]:
                    break
                ans = answer_query_rag(q, docs, embeddings, top_k=args.top_k)
                print("\n=== RESPOSTA DO MODELO ===")
                print(ans)
            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    main()
