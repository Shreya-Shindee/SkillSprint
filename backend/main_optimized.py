#!/usr/bin/env python3
"""
Optimized backend server with lazy ML model loading
"""
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routers import auth, skills, users, resources, progress, quiz, dashboard
import uvicorn

# Create FastAPI app
app = FastAPI(
    title="SkillSprint API",
    description="AI-Powered Adaptive Learning Platform API",
    version="1.0.0"
)

# Configure CORS
frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
origins = [
    frontend_url,
    "http://localhost:3000",  # React frontend default
    "http://localhost:3001",  # React alternate port
    "http://localhost:5173",  # Vite alternative
    "*",  # Allow all origins temporarily for debugging
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint (fast response)
@app.get("/")
@app.get("/health")
async def health_check():
    return {
        "message": "SkillSprint API is running!",
        "status": "healthy",
        "version": "1.0.0"
    }

# Quick test endpoint for authentication
@app.get("/auth/test")
async def test_auth():
    return {"message": "Auth endpoint is working"}

# Include routers
app.include_router(auth.router)
app.include_router(skills.router)
app.include_router(users.router)
app.include_router(resources.router)
app.include_router(progress.router)
app.include_router(quiz.router)
app.include_router(dashboard.router)

if __name__ == "__main__":
    # Get configuration from environment variables
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    debug = os.getenv("DEBUG", "True").lower() == "true"
    
    print(f"🚀 Starting SkillSprint API server on {host}:{port}")
    print(f"📊 Debug mode: {debug}")
    print(f"🌐 Frontend URL: {frontend_url}")
    print(f"🔐 Demo credentials: testuser / password123")
    print(f"📖 API docs: http://{host}:{port}/docs")
    
    uvicorn.run(
        "main_optimized:app",
        host=host, 
        port=port,
        reload=debug,
        log_level="info"
    )
