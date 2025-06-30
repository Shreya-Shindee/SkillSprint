"""
Cleanup Script for SkillSprint Codebase
---------------------------------------
This script removes redundant and unnecessary files from the codebase
to improve maintenance and reduce confusion.
"""

import os
import sys
import shutil
from pathlib import Path

# Files to be removed (relative to backend directory)
FILES_TO_REMOVE = [
    # Duplicate database utilities
    "database/check_db.py",
    "database/test_constraints.py",
    "check_db.py",
    "test_db_connection.py",
    "manage_db.ps1",
    
    # These are now consolidated into db_utils.py and test_db_operations.py
    "init_db.py",
    
    # Keep these for now for backward compatibility
    # "database/reset_db.py",
]

def cleanup():
    """Remove unnecessary files from the codebase."""
    # Get the backend directory
    backend_dir = Path(__file__).resolve().parent
    
    print(f"Starting cleanup in: {backend_dir}")
    print("-" * 50)
    
    removed_count = 0
    skipped_count = 0
    error_count = 0
    
    for file_path in FILES_TO_REMOVE:
        full_path = backend_dir / file_path
        if full_path.exists():
            try:
                if full_path.is_file():
                    full_path.unlink()
                elif full_path.is_dir():
                    shutil.rmtree(full_path)
                print(f"✅ Removed: {file_path}")
                removed_count += 1
            except Exception as e:
                print(f"❌ Error removing {file_path}: {e}")
                error_count += 1
        else:
            print(f"⚠️ File not found: {file_path}")
            skipped_count += 1
    
    print("-" * 50)
    print(f"Cleanup complete: {removed_count} removed, {skipped_count} skipped, {error_count} errors")
    
    # Create a .gitignore entry for __pycache__ folders
    gitignore_path = backend_dir / ".gitignore"
    try:
        with open(gitignore_path, "a+") as f:
            f.seek(0)
            content = f.read()
            if "__pycache__/" not in content:
                f.write("\n# Python cache files\n__pycache__/\n*.py[cod]\n*$py.class\n")
                print("✅ Updated .gitignore to exclude __pycache__ folders")
    except Exception as e:
        print(f"⚠️ Could not update .gitignore: {e}")
    
    return error_count == 0

if __name__ == "__main__":
    # Add a safety check to prevent accidental execution
    if len(sys.argv) > 1 and sys.argv[1] == "--confirm":
        success = cleanup()
        sys.exit(0 if success else 1)
    else:
        print("This script will remove the following files:")
        for file in FILES_TO_REMOVE:
            print(f"  - {file}")
        print("\nTo confirm and proceed, run: python cleanup.py --confirm")
        sys.exit(0)
