Write-Host "===============================================================" -ForegroundColor Cyan
Write-Host " LOCAL CI SCRIPT - pytest-demo" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/3] Linting with flake8..." -ForegroundColor Yellow
python -m flake8 --count --quiet --select=E9,F63,F7,f82 --show-source --statistics
if ($LASTEXITCODE -ne 0) {
    Write-Host "WARING: flake8 found issues (non-critical)." -ForegroundColor Magenta
} else{
    Write-Host "flake8 passed." -ForegroundColor Green
}
Write-Host ""

Write-Host "[2/3] Running tests with coverage..." -ForegroundColor Yellow
pytest -v --cov=calculator --cov-report=html --cov-report=term
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Tests failed!" -ForegroundColor Red
    exit 1
} else {
    Write-Host "All tests passed." -ForegroundColor Green
}
Write-Host ""

Write-Host "[3/3] Coverage report generated in htmlcov/index.html" -ForegroundColor Yellow
Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host " CI PASSED SUCCESSFULLY" -ForegroundColor Green
Write-Host "========================================="
