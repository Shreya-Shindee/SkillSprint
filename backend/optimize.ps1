# PowerShell script for optimizing the SkillSprint backend
# This script performs database reset, seed, and cleanup operations

Write-Host "SkillSprint Backend Optimization" -ForegroundColor Cyan
Write-Host "===============================" -ForegroundColor Cyan

# Get the current directory
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

# Step 1: Clear Python cache files
Write-Host "`nStep 1: Clearing Python cache files..." -ForegroundColor Yellow
python clear_cache.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "Warning: Cache clearing had some issues, but we'll continue." -ForegroundColor Yellow
}

# Step 2: Clean up redundant files
Write-Host "`nStep 2: Cleaning up redundant files..." -ForegroundColor Yellow
python cleanup.py --confirm
if ($LASTEXITCODE -ne 0) {
    Write-Host "Warning: Cleanup had some issues, but we'll continue." -ForegroundColor Yellow
}

# Step 3: Reset and seed the database with the new optimized utility
Write-Host "`nStep 3: Resetting and seeding database..." -ForegroundColor Yellow
python db_utils.py --reset --seed --fast
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Database reset and seed failed." -ForegroundColor Red
    exit 1
}

# Step 4: Run a final database check
Write-Host "`nStep 4: Performing final database check..." -ForegroundColor Yellow
python db_utils.py --check
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Database check failed." -ForegroundColor Red
    exit 1
}

Write-Host "`nOptimization complete! The SkillSprint backend has been optimized for better performance." -ForegroundColor Green
Write-Host "To start the backend server, run: python -m uvicorn main:app --reload" -ForegroundColor Cyan
