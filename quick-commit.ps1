#!/usr/bin/env pwsh
# 🚀 SkillSprint Quick Commit Script
# Usage: .\quick-commit.ps1 "Your commit message"

param(
    [Parameter(Mandatory=$true)]
    [string]$Message
)

Write-Host "🔍 Checking git status..." -ForegroundColor Blue
git status

Write-Host "`n📁 Adding all changes..." -ForegroundColor Blue
git add .

Write-Host "`n💾 Committing changes..." -ForegroundColor Blue
git commit -m $Message

Write-Host "`n🚀 Pushing to GitHub..." -ForegroundColor Blue
git push origin master

Write-Host "`n✅ Commit completed successfully!" -ForegroundColor Green
Write-Host "📊 Latest commits:" -ForegroundColor Yellow
git log --oneline -5
