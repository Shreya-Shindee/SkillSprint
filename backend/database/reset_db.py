"""
Reset the database by dropping all tables and recreating them.
This script handles the proper removal of data while respecting foreign key constraints.
"""
from database.database import engine, SessionLocal
from models.models import Base, User, Skill, Resource, SkillProgress, XPTransaction
from sqlalchemy import text
import traceback

def reset_db():
    db = SessionLocal()
    try:
        print("Attempting to truncate all tables with CASCADE...")
        try:
            # Make sure foreign key checks are enabled
            db.execute(text("SET CONSTRAINTS ALL IMMEDIATE"))
            
            # Use raw SQL to truncate all tables with CASCADE option
            # This is the safest way to clear all data while respecting foreign keys
            db.execute(text("TRUNCATE TABLE users, skills, resources, skill_progress, xp_transactions CASCADE"))
            db.commit()
            print("All data cleared successfully using TRUNCATE CASCADE.")
        except Exception as truncate_error:
            print(f"Error using TRUNCATE CASCADE: {truncate_error}")
            db.rollback()
            
            print("Attempting alternative approach - deleting data in proper order...")
            try:
                # Try deleting data in reverse order of dependencies
                db.execute(text("DELETE FROM xp_transactions"))
                db.execute(text("DELETE FROM skill_progress"))
                db.execute(text("DELETE FROM resources"))
                db.execute(text("DELETE FROM skills"))
                db.execute(text("DELETE FROM users"))
                db.commit()
                print("All data cleared successfully using DELETE statements.")
            except Exception as delete_error:
                print(f"Error using DELETE statements: {delete_error}")
                db.rollback()
                
                print("Falling back to dropping and recreating all tables...")
                # Close current session before dropping tables
                db.close()
                
                try:
                    # If all else fails, drop and recreate all tables
                    print("Dropping all tables...")
                    Base.metadata.drop_all(bind=engine)
                    print("Creating tables...")
                    Base.metadata.create_all(bind=engine)
                    print("Database reset complete using DROP and CREATE.")
                except Exception as schema_error:
                    print(f"Critical error: Could not reset database schema: {schema_error}")
                    traceback.print_exc()
                    return False
                return True
    except Exception as e:
        print(f"Unexpected error during database reset: {e}")
        traceback.print_exc()
        return False
    finally:
        db.close()
    
    print("Database reset complete.")
    return True

if __name__ == "__main__":
    import sys
    print("Starting database reset process...")
    success = reset_db()
    if success:
        print("Database reset completed successfully.")
        sys.exit(0)
    else:
        print("Database reset failed.")
        sys.exit(1)
