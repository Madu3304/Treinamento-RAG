# PowerShell script para conexao direta com as APIs do Hugging Face

Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "Conectando com a API do Hugging Face (Astronaut Database)" -ForegroundColor Cyan
Write-Host "=======================================================" -ForegroundColor Cyan

$baseDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# 1. Splits API
Write-Host "[1/3] Obtendo Splits da API..." -ForegroundColor Yellow
$splitsUrl = "https://datasets-server.huggingface.co/splits?dataset=juliensimon%2Fastronaut-database"
Invoke-RestMethod -Uri $splitsUrl -Method Get | ConvertTo-Json -Depth 10 | Set-Content (Join-Path $baseDir "splits.json") -Encoding UTF8

# 2. Parquet Info API
Write-Host "[2/3] Obtendo Parquet Info..." -ForegroundColor Yellow
$parquetUrl = "https://huggingface.co/api/datasets/juliensimon/astronaut-database/parquet/default/train"
Invoke-RestMethod -Uri $parquetUrl -Method Get | ConvertTo-Json -Depth 10 | Set-Content (Join-Path $baseDir "parquet_info.json") -Encoding UTF8

# 3. Rows API (Offset 0, Length 100)
Write-Host "[3/3] Obtendo Rows (Offset 0, Length 100)..." -ForegroundColor Yellow
$rowsUrl = "https://datasets-server.huggingface.co/rows?dataset=juliensimon%2Fastronaut-database&config=default&split=train&offset=0&length=100"
Invoke-RestMethod -Uri $rowsUrl -Method Get | ConvertTo-Json -Depth 10 | Set-Content (Join-Path $baseDir "rows_offset0_len100.json") -Encoding UTF8

Write-Host "=======================================================" -ForegroundColor Green
Write-Host "Concluido com sucesso! Arquivos salvos em $baseDir" -ForegroundColor Green
Write-Host "=======================================================" -ForegroundColor Green

