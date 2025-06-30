import sys
import os
import argparse

# Ensure we can import from the backend directory
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, backend_dir)

from database.database import engine, Base, SessionLocal
from models.models import User, Skill, Resource, SkillProgress, XPTransaction
# Note: quiz_models.py is empty, so we'll skip quiz model imports for now
from sqlalchemy import inspect

def init_db(force=False):
    """
    Initialize the database schema efficiently.
    
    Args:
        force: If True, recreate tables even if they already exist
    """
    db = SessionLocal()
    
    try:
        # Check if tables already exist
        inspector = inspect(engine)
        existing_tables = inspector.get_table_names()
        
        if existing_tables and not force:
            print(f"Database already contains {len(existing_tables)} tables")
            print("Use --force to recreate tables if needed")
            return True
        
        # Create tables
        print("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully")
        
        return True
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.close()

if __name__ == "__main__":
    # Check for force flag
    force = len(sys.argv) > 1 and sys.argv[1] == "--force"
    
    success = init_db(force=force)
    sys.exit(0 if success else 1)
