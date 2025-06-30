"""
PostgreSQL Database Setup Script for SkillSprint
This script helps set up the PostgreSQL database for development.
"""
import os
import subprocess
import sys
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database

def check_postgresql_service():
    """Check if PostgreSQL service is running"""
    try:
        # Try to connect to PostgreSQL default database
        engine = create_engine("postgresql://postgres@localhost/postgres")
        with engine.connect():
            print("✅ PostgreSQL service is running")
            return True
    except Exception as e:
        print(f"❌ PostgreSQL service not running or not accessible: {e}")
        print("Please ensure PostgreSQL is installed and running.")
        print("On Windows, you can start it with: net start postgresql-x64-13")
        return False

def create_database_and_user():
    """Create the SkillSprint database and user"""
    try:
        # Connect as postgres superuser (adjust if needed)
        admin_engine = create_engine("postgresql://postgres@localhost/postgres")
        
        with admin_engine.connect() as conn:
            # Use autocommit mode for database creation
            conn.execute(text("COMMIT"))
            
            # Create database if it doesn't exist
            try:
                conn.execute(text("CREATE DATABASE skillsprint_db"))
                print("✅ Created database: skillsprint_db")
            except Exception as e:
                if "already exists" in str(e):
                    print("ℹ️ Database skillsprint_db already exists")
                else:
                    raise e
            
            # Create user if it doesn't exist
            try:
                conn.execute(text("CREATE USER skillsprint_user WITH PASSWORD 'skillsprint_pass'"))
                print("✅ Created user: skillsprint_user")
            except Exception as e:
                if "already exists" in str(e):
                    print("ℹ️ User skillsprint_user already exists")
                else:
                    raise e
            
            # Grant privileges
            conn.execute(text("GRANT ALL PRIVILEGES ON DATABASE skillsprint_db TO skillsprint_user"))
            conn.execute(text("ALTER USER skillsprint_user CREATEDB"))
            print("✅ Granted privileges to skillsprint_user")
            
        admin_engine.dispose()
        return True
        
    except Exception as e:
        print(f"❌ Error creating database/user: {e}")
        print("You may need to:")
        print("1. Ensure PostgreSQL is installed and running")
        print("2. Connect as postgres superuser: postgresql://postgres@localhost/postgres")
        print("3. Or manually create the database and user")
        return False

def test_application_connection():
    """Test connection with application credentials"""
    try:
        db_url = "postgresql://skillsprint_user:skillsprint_pass@localhost/skillsprint_db"
        engine = create_engine(db_url)
        with engine.connect():
            print("✅ Successfully connected with application credentials")
            return True
    except Exception as e:
        print(f"❌ Failed to connect with application credentials: {e}")
        return False

def main():
    print("🐘 SkillSprint PostgreSQL Database Setup")
    print("=" * 40)
    
    # Check if PostgreSQL is running
    if not check_postgresql_service():
        print("\n❌ Setup failed: PostgreSQL service not available")
        sys.exit(1)
    
    # Create database and user
    if not create_database_and_user():
        print("\n❌ Setup failed: Could not create database/user")
        sys.exit(1)
    
    # Test application connection
    if not test_application_connection():
        print("\n❌ Setup failed: Application cannot connect to database")
        sys.exit(1)
    
    print("\n✅ PostgreSQL setup completed successfully!")
    print("\n📋 Database Configuration:")
    print("  Host: localhost")
    print("  Database: skillsprint_db")
    print("  User: skillsprint_user")
    print("  Password: skillsprint_pass")
    print("\n🔗 Connection String:")
    print("  postgresql://skillsprint_user:skillsprint_pass@localhost/skillsprint_db")
    print("\n🚀 Next steps:")
    print("  1. Install Python dependencies: pip install -r requirements.txt")
    print("  2. Initialize database: python -c \"from database.init_db import init_database; init_database()\"")
    print("  3. Start the application: python main.py")

if __name__ == "__main__":
    main()
