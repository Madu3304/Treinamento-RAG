@echo off
echo =======================================================
echo Conectando com a API do Hugging Face (Astronaut Database)
echo =======================================================

echo [1/3] Obtendo Splits da API...
curl.exe -s -X GET "https://datasets-server.huggingface.co/splits?dataset=juliensimon%%2Fastronaut-database" -o splits.json

echo [2/3] Obtendo Parquet Info...
curl.exe -s -X GET "https://huggingface.co/api/datasets/juliensimon/astronaut-database/parquet/default/train" -o parquet_info.json

echo [3/3] Obtendo Rows (Offset 0, Length 100)...
curl.exe -s -X GET "https://datasets-server.huggingface.co/rows?dataset=juliensimon%%2Fastronaut-database&config=default&split=train&offset=0&length=100" -o rows_offset0_len100.json

echo =======================================================
echo Concluido! Arquivos salvos com sucesso na pasta 3-api:
echo - splits.json
echo - parquet_info.json
echo - rows_offset0_len100.json
echo =======================================================

