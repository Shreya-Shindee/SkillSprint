"""
Simple FastAPI test server to debug CORS issues
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Test API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Test API is working"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/test")
def test_post():
    return {"message": "POST endpoint working"}

if __name__ == "__main__":
    print("🚀 Starting simple test server on port 8001")
    uvicorn.run("simple_test:app", host="0.0.0.0", port=8001, reload=True)
