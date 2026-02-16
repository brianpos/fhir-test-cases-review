# Repeatedly runs improve-tests.ps1 until cancelled (Ctrl+C), a stop.md file appears,
# or the maximum iteration count is reached.
#
# Usage: .\prompts\ralph.ps1 [-MaxIterations 200]
#
param(
    [int]$MaxIterations = 200
)

$stopFile = Join-Path $PSScriptRoot "..\stop.md"
$iteration = 0

$titles = @(
    "FHIRPath Ralph unit test fixerer.",
    'FHIRPath Ralph: "I''m helping!"',
    "FHIRPath Ralph: My tests are working! I'm a test!",
    "FHIRPath Ralph: I choo-choo-choose your tests.",
    "Hi, I'm Ralph! I fix tests good.",
    "FHIRPath Ralph: It tastes like burning (test gaps)."
)
$title = $titles | Get-Random

Write-Host ""
Write-Host "  ╔═════════════════════════════════════════════════════╗" -ForegroundColor Magenta
Write-Host "  ║  $($title.PadRight(50)) ║" -ForegroundColor Magenta
Write-Host "  ╚═════════════════════════════════════════════════════╝" -ForegroundColor Magenta
Write-Host ""
Write-Host "Starting improve-tests loop (max $MaxIterations iterations). Press Ctrl+C to cancel, or create stop.md to stop." -ForegroundColor Cyan

while ($true) {
    # Check for stop file before each iteration
    if (Test-Path $stopFile) {
        Write-Host "`nStop file detected: $stopFile" -ForegroundColor Yellow
        Write-Host (Get-Content $stopFile -Raw)
        Write-Host "Stopping." -ForegroundColor Yellow
        break
    }

    $iteration++
    Write-Host "`n========== Iteration $iteration — $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ==========" -ForegroundColor Green

    & "$PSScriptRoot\improve-tests.ps1"

    # Check for stop file after each iteration (may have been created by improve-tests.ps1)
    if (Test-Path $stopFile) {
        Write-Host "`nStop file created during iteration $iteration" -ForegroundColor Yellow
        Write-Host (Get-Content $stopFile -Raw)
        Write-Host "Stopping." -ForegroundColor Yellow
        break
    }

    Write-Host "Iteration $iteration complete. Pausing 5 seconds before next run..." -ForegroundColor Cyan

    if ($iteration -ge $MaxIterations) {
        Write-Host "`nMax iterations ($MaxIterations) reached." -ForegroundColor Yellow
        break
    }

    Start-Sleep -Seconds 5
}

Write-Host "`nCompleted after $iteration iteration(s)." -ForegroundColor Green
