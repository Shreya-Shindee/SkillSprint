"""
Clear Python Cache Files
-----------------------
This script removes all __pycache__ directories and .pyc files
to clean up the project and avoid stale cache issues.
"""

import os
import sys
import shutil
from pathlib import Path

def clear_pycache(directory):
    """
    Recursively remove all __pycache__ directories and .pyc files.
    
    Args:
        directory: Root directory to start search from
    """
    count = 0
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(directory):
        # Remove __pycache__ directories
        if "__pycache__" in dirs:
            pycache_dir = os.path.join(root, "__pycache__")
            try:
                shutil.rmtree(pycache_dir)
                print(f"Removed: {pycache_dir}")
                count += 1
            except Exception as e:
                print(f"Error removing {pycache_dir}: {e}")
        
        # Remove .pyc files
        for file in files:
            if file.endswith(".pyc") or file.endswith(".pyo") or file.endswith(".pyd"):
                pyc_file = os.path.join(root, file)
                try:
                    os.remove(pyc_file)
                    print(f"Removed: {pyc_file}")
                    count += 1
                except Exception as e:
                    print(f"Error removing {pyc_file}: {e}")
    
    return count

if __name__ == "__main__":
    # Get the project root directory
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]
    else:
        root_dir = Path(__file__).resolve().parent
    
    print(f"Clearing Python cache files in: {root_dir}")
    print("-" * 50)
    
    count = clear_pycache(root_dir)
    
    print("-" * 50)
    print(f"Cache cleanup complete: {count} items removed")
    print("This should help improve performance and avoid stale cache issues")
