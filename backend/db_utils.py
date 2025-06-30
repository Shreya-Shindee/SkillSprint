"""
SkillSprint Database Utility
----------------------------
A consolidated utility for database management operations in SkillSprint.

Usage:
    python db_utils.py [--reset] [--seed] [--check] [--fast] [--help]

Options:
    --reset     Reset database (clear all data)
    --seed      Seed database with sample data
    --check     Check database structure
    --fast      Use faster methods (skip some checks)
    --help      Show this help message
"""

import sys
import argparse
import os
from pathlib import Path

# Ensure backend directory is in the path so imports work correctly
backend_dir = Path(__file__).resolve().parent
if str(backend_dir) not in sys.path:
    sys.path.append(str(backend_dir))

# Now import the optimized database management function
from test_db_operations import db_manage

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SkillSprint Database Utility")
    parser.add_argument("--reset", action="store_true", help="Reset the database (clear all data)")
    parser.add_argument("--seed", action="store_true", help="Seed the database with sample data")
    parser.add_argument("--check", action="store_true", help="Check database structure")
    parser.add_argument("--fast", action="store_true", help="Use faster methods (skip some checks)")
    
    args = parser.parse_args()
    
    # If no args provided, show help
    if not any([args.reset, args.seed, args.check, args.fast]):
        print(__doc__)
        sys.exit(0)
    
    # Run the database management function with the provided options
    success = db_manage(
        reset=args.reset, 
        seed=args.seed, 
        check=args.check,
        fast=args.fast
    )
    
    sys.exit(0 if success else 1)
