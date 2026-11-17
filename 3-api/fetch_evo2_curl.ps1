# PowerShell script para conexao direta com a API do Hugging Face para jang1563/evo2-spaceflight-vep

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Conectando com a API do Hugging Face: jang1563/evo2-spaceflight-vep" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan

$baseDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# 1. Splits
Write-Host "[1/2] Obtendo Splits..." -ForegroundColor Yellow
$splitsUrl = "https://datasets-server.huggingface.co/splits?dataset=jang1563%2Fevo2-spaceflight-vep"
Invoke-RestMethod -Uri $splitsUrl -Method Get | ConvertTo-Json -Depth 10 | Set-Content (Join-Path $baseDir "evo2_splits.json") -Encoding UTF8

# 2. First Rows
Write-Host "[2/2] Obtendo First Rows..." -ForegroundColor Yellow
$rowsUrl = "https://datasets-server.huggingface.co/first-rows?dataset=jang1563%2Fevo2-spaceflight-vep&config=default&split=train"
Invoke-RestMethod -Uri $rowsUrl -Method Get | ConvertTo-Json -Depth 10 | Set-Content (Join-Path $baseDir "evo2_first_rows.json") -Encoding UTF8

Write-Host "======================================================================" -ForegroundColor Green
Write-Host "Concluido com sucesso! Arquivos salvos em $baseDir" -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Green

