@echo off
echo ======================================================================
echo Conectando com a API do Hugging Face: jang1563/evo2-spaceflight-vep
echo ======================================================================

echo [1/2] Obtendo Splits...
curl.exe -s -X GET "https://datasets-server.huggingface.co/splits?dataset=jang1563%%2Fevo2-spaceflight-vep" -o evo2_splits.json

echo [2/2] Obtendo First Rows...
curl.exe -s -X GET "https://datasets-server.huggingface.co/first-rows?dataset=jang1563%%2Fevo2-spaceflight-vep&config=default&split=train" -o evo2_first_rows.json

echo ======================================================================
echo Concluido! Arquivos salvos com sucesso na pasta 3-api:
echo - evo2_splits.json
echo - evo2_first_rows.json
echo ======================================================================

