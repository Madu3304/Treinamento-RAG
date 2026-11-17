"""
Script utilitário para conectar, sincronizar e unir datasets armazenados no Google Drive
com o ecossistema local do Treinamento-RAG.
"""

import os
import sys
import shutil
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOCAL_KNOWLEDGE = BASE_DIR / "1-ia-base-conhecimento"
LOCAL_NASA = BASE_DIR / "2-DATASET-NASA"
LOCAL_API = BASE_DIR / "3-api"

def check_local_gdrive_desktop():
    """Verifica se o Google Drive for Desktop está montado em unidades virtuais comuns (Windows: G:, H:, etc.)."""
    common_drives = ["G:", "H:", "I:", "D:", "E:"]
    found = []
    for d in common_drives:
        path = Path(f"{d}\\Meu Drive")
        if path.exists():
            found.append(path)
        path_en = Path(f"{d}\\My Drive")
        if path_en.exists():
            found.append(path_en)
    return found

def merge_from_folder(source_folder: Path, destination_folder: Path, dry_run=False):
    """Copia e une arquivos novos/atualizados de uma pasta do Drive para a pasta local correspondente."""
    if not source_folder.exists():
        print(f"[ERRO] Pasta de origem não encontrada: {source_folder}")
        return

    print(f"\n[Sincronizando] De: {source_folder} -> Para: {destination_folder}")
    copied = 0
    skipped = 0

    for item in source_folder.rglob("*"):
        if item.is_file():
            rel_path = item.relative_to(source_folder)
            dest_file = destination_folder / rel_path

            # Pula arquivos temporários ou de sistema
            if item.name.startswith("~$") or item.name == "desktop.ini":
                continue

            dest_file.parent.mkdir(parents=True, exist_ok=True)

            # Verifica se precisa copiar (se não existe ou se foi modificado)
            if not dest_file.exists() or item.stat().st_mtime > dest_file.stat().st_mtime:
                if not dry_run:
                    shutil.copy2(item, dest_file)
                print(f"  + [NOVO/ATUALIZADO] {rel_path}")
                copied += 1
            else:
                skipped += 1

    print(f"[Resumo] Copiados/Atualizados: {copied} | Já existentes: {skipped}")

def main():
    parser = argparse.ArgumentParser(description="Sincronizador e Integrador de Datasets do Google Drive com Treinamento-RAG")
    parser.add_argument("--source", "-s", type=str, help="Caminho da pasta do Google Drive contendo os datasets")
    parser.add_argument("--target", "-t", type=str, choices=["1-ia-base-conhecimento", "2-DATASET-NASA", "3-api"], default="2-DATASET-NASA", help="Pasta destino no projeto local")
    parser.add_argument("--dry-run", action="store_true", help="Simula as ações sem copiar arquivos")
    args = parser.parse_args()

    print("=== Sincronizador de Datasets Google Drive -> Treinamento-RAG ===")
    
    if args.source:
        src = Path(args.source)
        dest = BASE_DIR / args.target
        merge_from_folder(src, dest, dry_run=args.dry_run)
    else:
        detected = check_local_gdrive_desktop()
        if detected:
            print(f"[Google Drive Detectado]: {detected[0]}")
            print("\nPara sincronizar, execute:")
            print(f'python sync_gdrive.py --source "{detected[0]}\\NASA_DATASETS" --target 2-DATASET-NASA')
        else:
            print("[Info] Google Drive for Desktop não detectado automaticamente em unidades G: ou H:.")
            print("Informe o caminho manualmente usando o argumento --source:")
            print('python sync_gdrive.py --source "C:\\Users\\User\\Google Drive\\Meus_Datasets" --target 2-DATASET-NASA')

if __name__ == "__main__":
    main()

