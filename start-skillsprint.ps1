#!/usr/bin/env pwsh
# SkillSprint Complete Startup Script
# This script starts both backend and frontend services

Write-Host "🚀 SkillSprint AI-Powered Adaptive Learning Platform" -ForegroundColor Green
Write-Host "=================================================" -ForegroundColor Green

# Function to check if a port is in use
function Test-Port {
    param([int]$Port)
    try {
        $connection = New-Object System.Net.Sockets.TcpClient
        $connection.Connect("localhost", $Port)
        $connection.Close()
        return $true
    } catch {
        return $false
    }
}

# Check prerequisites
Write-Host "📋 Checking prerequisites..." -ForegroundColor Yellow

# Check Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Check Node.js
try {
    $nodeVersion = node --version 2>&1
    Write-Host "✅ Node.js: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Node.js not found. Please install Node.js 16+" -ForegroundColor Red
    exit 1
}

# Check if backend is already running
if (Test-Port 8000) {
    Write-Host "⚠️ Backend is already running on port 8000" -ForegroundColor Yellow
} else {
    Write-Host "🔧 Starting Backend Server..." -ForegroundColor Cyan
    
    # Start backend in a new PowerShell window
    $backendPath = "e:\shreya shinde\projects\SkillSprint\backend"
    $backendCommand = "cd '$backendPath'; if (Test-Path 'venv\Scripts\Activate.ps1') { & 'venv\Scripts\Activate.ps1' }; python main.py"
    
    Start-Process powershell -ArgumentList "-NoExit", "-Command", $backendCommand
    
    # Wait for backend to start
    Write-Host "⏳ Waiting for backend to start..." -ForegroundColor Yellow
    $timeout = 30
    $elapsed = 0
    while (-not (Test-Port 8000) -and $elapsed -lt $timeout) {
        Start-Sleep -Seconds 1
        $elapsed++
        Write-Host "." -NoNewline
    }
    
    if (Test-Port 8000) {
        Write-Host "`n✅ Backend started on http://localhost:8000" -ForegroundColor Green
    } else {
        Write-Host "`n❌ Backend failed to start within $timeout seconds" -ForegroundColor Red
        exit 1
    }
}

# Check frontend ports
$frontendPort = 3001
if (Test-Port 3000) {
    Write-Host "⚠️ Port 3000 is already in use, using port 3001" -ForegroundColor Yellow
    $frontendPort = 3001
} else {
    $frontendPort = 3000
}

if (Test-Port $frontendPort) {
    Write-Host "⚠️ Frontend is already running on port $frontendPort" -ForegroundColor Yellow
} else {
    Write-Host "🎨 Starting Frontend Server on port $frontendPort..." -ForegroundColor Cyan
    
    # Start frontend in a new PowerShell window
    $frontendPath = "e:\shreya shinde\projects\SkillSprint\frontend"
    $frontendCommand = "cd '$frontendPath'; `$env:PORT='$frontendPort'; npm start"
    
    Start-Process powershell -ArgumentList "-NoExit", "-Command", $frontendCommand
    
    # Wait for frontend to start
    Write-Host "⏳ Waiting for frontend to start..." -ForegroundColor Yellow
    $timeout = 60
    $elapsed = 0
    while (-not (Test-Port $frontendPort) -and $elapsed -lt $timeout) {
        Start-Sleep -Seconds 2
        $elapsed += 2
        Write-Host "." -NoNewline
    }
    
    if (Test-Port $frontendPort) {
        Write-Host "`n✅ Frontend started on http://localhost:$frontendPort" -ForegroundColor Green
    } else {
        Write-Host "`n❌ Frontend failed to start within $timeout seconds" -ForegroundColor Red
    }
}

Write-Host "`n🎉 SkillSprint is now running!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host "🌐 Frontend: http://localhost:$frontendPort" -ForegroundColor Cyan
Write-Host "🔗 Backend API: http://localhost:8000" -ForegroundColor Cyan
Write-Host "📚 API Documentation: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "👤 Demo User Credentials:" -ForegroundColor Yellow
Write-Host "   Username: testuser" -ForegroundColor White
Write-Host "   Password: password123" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C in the backend or frontend terminal windows to stop the servers." -ForegroundColor Gray

# Optional: Open browser
$response = Read-Host "Would you like to open the application in your default browser? (Y/n)"
if ($response -eq "" -or $response.ToLower() -eq "y") {
    Start-Process "http://localhost:$frontendPort"
}
