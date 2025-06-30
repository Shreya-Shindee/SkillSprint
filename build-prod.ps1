#!/usr/bin/env pwsh
# SkillSprint Production Build Script
# This script builds the application for production deployment

Write-Host "🏗️ SkillSprint Production Build" -ForegroundColor Green
Write-Host "===============================" -ForegroundColor Green

# Build Backend
Write-Host "🔧 Building Backend..." -ForegroundColor Yellow
Set-Location "backend"

# Activate virtual environment
if (Test-Path "venv\Scripts\Activate.ps1") {
    Write-Host "⚡ Activating virtual environment..." -ForegroundColor Cyan
    & "venv\Scripts\Activate.ps1"
} else {
    Write-Host "❌ Virtual environment not found. Run fast-start.ps1 first." -ForegroundColor Red
    exit 1
}

# Install production dependencies
Write-Host "📦 Installing production dependencies..." -ForegroundColor Cyan
pip install -r requirements.txt --no-dev

# Run database migrations/setup
Write-Host "🗄️ Setting up production database..." -ForegroundColor Cyan
python -c "from database.init_db import init_database; init_database()"

# Build Frontend
Write-Host "🔧 Building Frontend..." -ForegroundColor Yellow
Set-Location "..\frontend"

# Install dependencies
Write-Host "📦 Installing Node.js dependencies..." -ForegroundColor Cyan
npm ci --production

# Build for production
Write-Host "🏗️ Building React application..." -ForegroundColor Cyan
npm run build

# Return to root directory
Set-Location ".."

# Create production directory structure
Write-Host "📁 Creating production build structure..." -ForegroundColor Cyan
if (!(Test-Path "dist")) {
    New-Item -ItemType Directory -Name "dist"
}

# Copy backend files
Write-Host "📋 Copying backend files..." -ForegroundColor Cyan
Copy-Item -Path "backend\*" -Destination "dist\" -Recurse -Force -Exclude "venv", "__pycache__", "*.pyc"

# Copy frontend build
Write-Host "📋 Copying frontend build..." -ForegroundColor Cyan
Copy-Item -Path "frontend\build\*" -Destination "dist\static\" -Recurse -Force

# Create production start script
Write-Host "📄 Creating production start script..." -ForegroundColor Cyan
$startScript = @"
#!/usr/bin/env pwsh
# Production Start Script
Write-Host "🚀 Starting SkillSprint Production Server..." -ForegroundColor Green
Set-Location "dist"
python main.py --host 0.0.0.0 --port 8000
"@

$startScript | Out-File -FilePath "dist\start-production.ps1" -Encoding UTF8

Write-Host "✅ Production Build Complete!" -ForegroundColor Green
Write-Host ""
Write-Host "📁 Production files are in the 'dist' directory" -ForegroundColor Cyan
Write-Host "🚀 Run 'dist\start-production.ps1' to start the production server" -ForegroundColor Cyan
Write-Host ""
Write-Host "Production server will run on: http://localhost:8000" -ForegroundColor Yellow
