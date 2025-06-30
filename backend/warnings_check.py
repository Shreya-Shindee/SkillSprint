#!/usr/bin/env python3
"""
Quick verification that original warnings are resolved
"""
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("Testing for original warnings...")

print("Database imports...")
try:
    from database.database import engine, SessionLocal
    print(" Database imports OK")
except Exception as e:
    print(f" Database imports failed: {e}")

print("Models imports...")
try:
    from models.models import User, Skill
    print(" Models imports OK")
except Exception as e:
    print(f" Models imports failed: {e}")

print("Utils imports...")
try:
    from utils.auth import get_current_user
    print(" Utils imports OK")
except Exception as e:
    print(f" Utils imports failed: {e}")

print("Checking for sentence_transformers...")
try:
    from sentence_transformers import SentenceTransformer
    print(" ✓ sentence_transformers imported successfully")
except Exception as e:
    print(f" Warning: sentence_transformers could not be imported. Using fallback methods.")

print("Router imports...")
try:
    from app.routers import auth, skills, users, resources, progress, quiz
    print(" Router imports OK")
except Exception as e:
    print(f" Router imports failed: {e}")

print("\nTest complete!")
