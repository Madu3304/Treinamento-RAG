import os
import json
import requests
import pandas as pd

API_SPLITS = "https://datasets-server.huggingface.co/splits?dataset=juliensimon%2Fastronaut-database"
API_PARQUET = "https://huggingface.co/api/datasets/juliensimon/astronaut-database/parquet/default/train"
API_ROWS_BASE = "https://datasets-server.huggingface.co/rows?dataset=juliensimon%2Fastronaut-database&config=default&split=train"

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

def fetch_json(url):
    print(f"Fetching: {url}")
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()

def main():
    print("=== 1. Coletando Splits da API do Hugging Face ===")
    splits_data = fetch_json(API_SPLITS)
    splits_path = os.path.join(OUTPUT_DIR, "splits.json")
    with open(splits_path, "w", encoding="utf-8") as f:
        json.dump(splits_data, f, indent=2, ensure_ascii=False)
    print(f"Salvo em: {splits_path}")

    print("\n=== 2. Coletando Metadados Parquet da API do Hugging Face ===")
    parquet_data = fetch_json(API_PARQUET)
    parquet_index_path = os.path.join(OUTPUT_DIR, "parquet_info.json")
    with open(parquet_index_path, "w", encoding="utf-8") as f:
        json.dump(parquet_data, f, indent=2, ensure_ascii=False)
    print(f"Salvo em: {parquet_index_path}")

    # Baixar arquivo parquet direto se disponivel
    if isinstance(parquet_data, list) and len(parquet_data) > 0:
        parquet_url = parquet_data[0]
        print(f"Baixando arquivo Parquet de: {parquet_url}")
        pq_res = requests.get(parquet_url, timeout=60)
        if pq_res.status_code == 200:
            parquet_file_path = os.path.join(OUTPUT_DIR, "astronauts.parquet")
            with open(parquet_file_path, "wb") as f:
                f.write(pq_res.content)
            print(f"Arquivo Parquet salvo em: {parquet_file_path}")

    print("\n=== 3. Coletando Rows (Offset 0, Length 100) ===")
    first_page_url = f"{API_ROWS_BASE}&offset=0&length=100"
    first_page_data = fetch_json(first_page_url)
    first_page_path = os.path.join(OUTPUT_DIR, "rows_offset0_len100.json")
    with open(first_page_path, "w", encoding="utf-8") as f:
        json.dump(first_page_data, f, indent=2, ensure_ascii=False)
    print(f"Salvo em: {first_page_path}")

    total_rows = first_page_data.get("num_rows_total", 870)
    print(f"\nTotal de astronautas no dataset: {total_rows}")

    print("\n=== 4. Coletando Todos os Registros do Dataset (Paginação Completa) ===")
    all_astronauts = []
    # Já temos a primeira página
    for item in first_page_data.get("rows", []):
        all_astronauts.append(item.get("row", {}))

    offset = 100
    page_size = 100
    while offset < total_rows:
        page_url = f"{API_ROWS_BASE}&offset={offset}&length={page_size}"
        page_data = fetch_json(page_url)
        rows = page_data.get("rows", [])
        if not rows:
            break
        for item in rows:
            all_astronauts.append(item.get("row", {}))
        print(f"Progresso: {len(all_astronauts)}/{total_rows} astronautas coletados...")
        offset += page_size

    # Salva dataset consolidado em JSON
    all_json_path = os.path.join(OUTPUT_DIR, "astronauts_complete.json")
    with open(all_json_path, "w", encoding="utf-8") as f:
        json.dump(all_astronauts, f, indent=2, ensure_ascii=False)
    print(f"Dataset completo salvo em: {all_json_path} ({len(all_astronauts)} registros)")

    # Salva também em CSV para facilitar visualização e análise
    df = pd.DataFrame(all_astronauts)
    csv_path = os.path.join(OUTPUT_DIR, "astronauts.csv")
    df.to_csv(csv_path, index=False, encoding="utf-8")
    print(f"Dataset salvo em CSV: {csv_path}")

    print("\n[OK] Conexao com as APIs concluida e dados salvos com sucesso!")

if __name__ == "__main__":
    main()

