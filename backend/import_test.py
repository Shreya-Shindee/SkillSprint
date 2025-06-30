import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("Testing imports for warnings...")

try:
    print("Database imports...")
    from database.database import engine, SessionLocal
    print(" ✓ Database imports OK")
except Exception as e:
    print(f" ❌ Database imports failed: {e}")

try:
    print("Models imports...")
    from models.models import User, Skill
    print(" ✓ Models imports OK")
except Exception as e:
    print(f" ❌ Models imports failed: {e}")

try:
    print("Utils imports...")
    from utils.auth import get_current_user
    print(" ✓ Utils imports OK")
except Exception as e:
    print(f" ❌ Utils imports failed: {e}")

try:
    print("Schema imports...")
    from schemas.schemas import UserResponse
    print(" ✓ Schema imports OK")
except Exception as e:
    print(f" ❌ Schema imports failed: {e}")

try:
    print("Sentence transformers import...")
    from sentence_transformers import SentenceTransformer
    print(" ✓ Sentence transformers import OK")
except Exception as e:
    print(f" ⚠️ Warning: sentence_transformers could not be imported. Using fallback methods.")

try:
    print("Router imports...")
    from app.routers import auth, skills, users, resources, progress, quiz
    print(" ✓ Router imports OK")
except Exception as e:
    print(f" ❌ Router imports failed: {e}")

print("\nImport test complete!")
