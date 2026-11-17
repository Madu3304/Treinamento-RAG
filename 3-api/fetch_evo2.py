import os
import json
import requests

API_SPLITS = "https://datasets-server.huggingface.co/splits?dataset=jang1563%2Fevo2-spaceflight-vep"
API_FIRST_ROWS = "https://datasets-server.huggingface.co/first-rows?dataset=jang1563%2Fevo2-spaceflight-vep&config=default&split=train"

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

def fetch_and_save(url, output_filename):
    print(f"[Conectando] {url}")
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    data = response.json()
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[Salvo com sucesso] {output_path}")
    return data

def main():
    print("=== Conectando com a API do Hugging Face: jang1563/evo2-spaceflight-vep ===")
    
    # 1. Splits
    fetch_and_save(API_SPLITS, "evo2_splits.json")
    
    # 2. First Rows
    fetch_and_save(API_FIRST_ROWS, "evo2_first_rows.json")
    
    print("\n[OK] Conexao com as APIs concluida e arquivos salvos na pasta 3-api!")

if __name__ == "__main__":
    main()

