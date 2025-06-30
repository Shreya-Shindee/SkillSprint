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

# Root endpoint for testing
@app.get("/")
async def root():
    return {
        "status": "API is running", 
        "message": "Welcome to SkillSprint AI-Powered Adaptive Learning Platform",
        "version": "1.0.0",
        "features": [
            "AI-powered skill decomposition",
            "Adaptive quiz generation",
            "Collaborative filtering recommendations",
            "Dynamic difficulty adjustment",
            "Gamified progress tracking",
            "Behavioral learning analytics"
        ]
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": "2024-01-01T00:00:00Z"}

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(skills.router)
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
    
    uvicorn.run(
        "main:app",  # Use module:app format for reload to work properly
        host=host, 
        port=port,
        reload=debug,
        log_level="debug" if debug else "info"
    )
