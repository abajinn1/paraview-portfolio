$ErrorActionPreference = "Stop"
$repo = "$HOME\opm-data\norne"
Push-Location $repo

Write-Host "NORNE MODEL | COMMAND-LINE WORKFLOW SUMMARY"
Write-Host "==========================================="
Write-Host ""

Write-Host "[1] Conversion command"
Write-Host "py em2ex.py -f NORNE_PORTFOLIO.grdecl"
$conv = py $HOME\em2ex\em2ex.py -f NORNE_PORTFOLIO.grdecl 2>&1
$conv | Where-Object { $_ -match "Reading|Exodus file written" } | ForEach-Object { Write-Host $_ }
Write-Host ""

Write-Host "[2] Output file check"
Get-Item .\NORNE_PORTFOLIO.e | Select-Object Name, Length, LastWriteTime | Format-Table -AutoSize
Write-Host ""

Write-Host "[3] Analysis report"
Get-Content "$HOME\Documents\GitHub\paraview-portfolio\assets\project1-norne\p1-analysis-report.txt"

Pop-Location
