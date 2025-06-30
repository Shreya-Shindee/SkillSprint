# Database Management in SkillSprint

This document describes the optimized database management utilities and best practices for the SkillSprint project.

## Streamlined Database Management

The SkillSprint backend now includes a unified database utility for faster and more reliable database operations:

### `db_utils.py`

This consolidated utility provides all database management functions in one place:

- **Features**:
  - Faster database operations with `--fast` option
  - Combined reset, seed, and check operations
  - Improved error handling and recovery
  - Reduced dependency on external files

- **Usage**:
  ```powershell
  # All-in-one database setup (reset, seed, and check)
  python db_utils.py --reset --seed --check

  # For faster operations
  python db_utils.py --reset --seed --fast

  # Individual operations
  python db_utils.py --reset   # Only reset database
  python db_utils.py --seed    # Only seed data
  python db_utils.py --check   # Only check structure
  ```

### `test_db_operations.py`

This is the core implementation that `db_utils.py` uses. It provides a unified `db_manage()` function that handles all database operations efficiently.

## Optimization Scripts

### `optimize.ps1`

A PowerShell script that runs all optimization steps in sequence:

1. Clears Python cache files
2. Removes redundant files
3. Resets and seeds the database with unique resources
4. Performs a final database check

Run it with:
```powershell
.\optimize.ps1
```

### Resource Verification

After optimization, all resources have unique URLs:
- **Documentation**: Python Official Tutorial (`https://docs.python.org/3/tutorial/`)
- **Article**: Python Basics on Real Python (`https://realpython.com/python-basics/`)
- **Course**: Python for Everybody on Coursera (`https://www.coursera.org/specializations/python`)

Use `python verify_resources.py` to verify resource uniqueness at any time.

### `clear_cache.py`

Removes Python cache files (`__pycache__` directories and `.pyc` files) to improve loading time and avoid stale cache issues.

### `cleanup.py`

Removes redundant files from the codebase to reduce confusion and improve maintainability.

## Legacy Support

For backward compatibility, the following files are still available but will be deprecated in future versions:

- `database/reset_db.py`
- `database/seed_data.py`
- `database/init_db.py`

## Performance Improvements

The new database utilities include several performance optimizations:

1. **Connection Pooling**: Optimized database connections with connection pooling
2. **Retry Logic**: Automatic retry for transient database errors
3. **Fast Operations**: The `--fast` option skips non-essential checks
4. **Better Error Handling**: More robust error handling and recovery

## Database Structure

The SkillSprint database includes the following main tables:

- `users` - User accounts and authentication data
- `skills` - Skills and subskills forming the skill hierarchy
- `resources` - Learning resources linked to skills
- `skill_progress` - User progress for each skill
- `xp_transactions` - Experience points earned by users

## Best Practices

1. **Use the new utilities**: Prefer `db_utils.py` over the legacy scripts
2. **Clean cache regularly**: Run `clear_cache.py` if you encounter import or stale data issues
3. **Consider using `--fast`**: For development environments where speed is more important than thorough checks
4. **Always backup production data** before running reset operations
