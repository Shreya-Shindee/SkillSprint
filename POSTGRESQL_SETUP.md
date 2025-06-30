# PostgreSQL Installation Guide for SkillSprint

## 🐘 Installing PostgreSQL on Windows

### Option 1: Official PostgreSQL Installer (Recommended)

1. **Download PostgreSQL**:
   - Visit: https://www.postgresql.org/download/windows/
   - Download the latest version (15.x or 16.x)
   - Choose the Windows x86-64 installer

2. **Install PostgreSQL**:
   - Run the installer as Administrator
   - Use these settings:
     - Installation Directory: `C:\Program Files\PostgreSQL\15` (default)
     - Data Directory: `C:\Program Files\PostgreSQL\15\data` (default)
     - Password: Choose a strong password for postgres user (remember this!)
     - Port: `5432` (default)
     - Locale: Default locale

3. **Verify Installation**:
   ```powershell
   # Check if PostgreSQL service is running
   Get-Service postgresql*
   
   # Test connection
   psql -U postgres -c "SELECT version();"
   ```

### Option 2: Using Chocolatey (If you have Chocolatey installed)

```powershell
# Install PostgreSQL
choco install postgresql

# Start the service
net start postgresql-x64-15
```

### Option 3: Using Docker (Alternative)

```powershell
# Pull and run PostgreSQL in Docker
docker run --name skillsprint-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:15

# Create application database
docker exec -it skillsprint-postgres psql -U postgres -c "CREATE DATABASE skillsprint_db;"
```

## 🔧 Database Setup for SkillSprint

After installing PostgreSQL, run our setup script:

```powershell
cd backend
python database_setup.py
```

Or set it up manually:

1. **Connect to PostgreSQL**:
   ```powershell
   psql -U postgres
   ```

2. **Create Database and User**:
   ```sql
   -- Create database
   CREATE DATABASE skillsprint_db;
   
   -- Create user
   CREATE USER skillsprint_user WITH PASSWORD 'skillsprint_pass';
   
   -- Grant privileges
   GRANT ALL PRIVILEGES ON DATABASE skillsprint_db TO skillsprint_user;
   ALTER USER skillsprint_user CREATEDB;
   
   -- Exit
   \q
   ```

3. **Test Connection**:
   ```powershell
   psql -h localhost -U skillsprint_user -d skillsprint_db -c "SELECT 'Connection successful!';"
   ```

## 🚀 Quick Start (If PostgreSQL is already installed)

```powershell
# 1. Navigate to backend directory
cd backend

# 2. Activate virtual environment
venv\Scripts\Activate.ps1

# 3. Install dependencies (including PostgreSQL adapter)
pip install -r requirements.txt

# 4. Setup database
python database_setup.py

# 5. Start the application
python main.py
```

## 🔄 Alternative: Use SQLite for Development

If you prefer to use SQLite (simpler setup), update your `.env` file:

```env
# Change this line in backend/.env
DATABASE_URL=sqlite:///./skillsprint.db
```

Then run:
```powershell
python database_setup.py
```

## 🛠️ Troubleshooting

### Issue: "psql is not recognized"
- Add PostgreSQL bin directory to PATH: `C:\Program Files\PostgreSQL\15\bin`

### Issue: "Connection refused"
- Start PostgreSQL service: `net start postgresql-x64-15`
- Check if PostgreSQL is listening on port 5432

### Issue: "Authentication failed"
- Verify username/password in connection string
- Check `pg_hba.conf` for authentication settings

### Issue: "Database does not exist"
- Run the database creation commands manually
- Or use our automated setup script

## 📊 Verification

After setup, verify everything works:

```powershell
# Check database connection
python -c "from database.database import engine; print('✅ Database connected successfully!' if engine else '❌ Connection failed')"

# Start the application
python main.py
```

Visit http://localhost:8000/docs to see the API documentation.
