"""
SkillSprint Database Setup and Health Check
Supports both PostgreSQL and SQLite based on environment configuration
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_database_setup():
    """Check and setup database based on environment configuration"""
    database_url = os.getenv("DATABASE_URL", "sqlite:///./skillsprint.db")
    
    print("🗄️ SkillSprint Database Setup")
    print("=" * 30)
    print(f"Database URL: {database_url}")
    
    if database_url.startswith("postgresql"):
        return setup_postgresql()
    else:
        return setup_sqlite()

def setup_postgresql():
    """Setup PostgreSQL database"""
    print("\n🐘 Setting up PostgreSQL...")
    
    try:
        from sqlalchemy import create_engine, text
        
        database_url = os.getenv("DATABASE_URL")
        print(f"Connecting to: {database_url}")
        
        # Try to connect
        engine = create_engine(database_url)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        
        print("✅ PostgreSQL connection successful!")
        return True
        
    except ImportError:
        print("❌ psycopg2 not installed. Install with: pip install psycopg2-binary")
        return False
    except Exception as e:
        print(f"❌ PostgreSQL connection failed: {e}")
        print("\n📋 PostgreSQL Setup Instructions:")
        print("1. Install PostgreSQL: https://www.postgresql.org/download/")
        print("2. Start PostgreSQL service")
        print("3. Create database and user:")
        print("   - Connect to PostgreSQL: psql -U postgres")
        print("   - CREATE DATABASE skillsprint_db;")
        print("   - CREATE USER skillsprint_user WITH PASSWORD 'skillsprint_pass';")
        print("   - GRANT ALL PRIVILEGES ON DATABASE skillsprint_db TO skillsprint_user;")
        print("   - ALTER USER skillsprint_user CREATEDB;")
        return False

def setup_sqlite():
    """Setup SQLite database"""
    print("\n📄 Setting up SQLite...")
    
    try:
        from sqlalchemy import create_engine
        
        database_url = os.getenv("DATABASE_URL", "sqlite:///./skillsprint.db")
        print(f"Database file: {database_url}")
        
        # Create engine to test connection
        engine = create_engine(database_url, connect_args={"check_same_thread": False})
        with engine.connect():
            pass
        
        print("✅ SQLite setup successful!")
        return True
        
    except Exception as e:
        print(f"❌ SQLite setup failed: {e}")
        return False

def initialize_database_schema():
    """Initialize database schema with tables"""
    print("\n🔧 Initializing database schema...")
    
    try:
        # Import database initialization
        from database.init_db import init_db
        init_db(force=True)
        print("✅ Database schema initialized!")
        return True
        
    except Exception as e:
        print(f"❌ Schema initialization failed: {e}")
        print("Make sure all dependencies are installed: pip install -r requirements.txt")
        return False

def main():
    """Main setup function"""
    # Check database setup
    if not check_database_setup():
        print("\n❌ Database setup failed!")
        return False
    
    # Initialize schema
    if not initialize_database_schema():
        print("\n❌ Schema initialization failed!")
        return False
    
    print("\n✅ Database setup completed successfully!")
    print("\n🚀 Ready to start the application!")
    print("Run: python main.py")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
