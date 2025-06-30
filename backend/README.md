# SkillSprint Backend Setup and Run Instructions

## Prerequisites
- Python 3.8 or higher
- PostgreSQL database

## Setup Steps

1. Create a virtual environment:
```
python -m venv venv
```

2. Activate the virtual environment:
```
# On Windows
venv\Scripts\activate

# On MacOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Configure the database:
   - Create a PostgreSQL database named `skillsprint`
   - Update the database connection URL in `database/database.py` if needed

5. Initialize and manage the database (new streamlined approach):
```
# All-in-one database setup (reset, seed, and check)
python db_utils.py --reset --seed --check

# For faster operations
python db_utils.py --reset --seed --fast

# Individual operations
python db_utils.py --reset   # Only reset database
python db_utils.py --seed    # Only seed data
python db_utils.py --check   # Only check structure
```

7. Run the application:
```
uvicorn main:app --reload
```

8. Access the API documentation:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## API Endpoints

- **Authentication**:
  - POST `/auth/register`: Register a new user
  - POST `/auth/token`: Login and get access token

- **Users**:
  - GET `/users/me`: Get current user information
  - GET `/users/xp`: Get user's total XP
  - GET `/users/xp/history`: Get user's XP transaction history

- **Skills**:
  - GET `/skills/`: List all skills
  - GET `/skills/{skill_id}`: Get a specific skill
  - POST `/skills/`: Create a new skill
  - POST `/skills/decompose`: Decompose a skill into subskills
  - POST `/skills/learning-path`: Generate a learning path for a skill

- **Resources**:
  - GET `/resources/`: List all resources
  - GET `/resources/{resource_id}`: Get a specific resource
  - GET `/resources/skill/{skill_id}`: Get resources for a specific skill
  - POST `/resources/`: Create a new resource

- **Progress**:
  - GET `/progress/`: Get all progress entries for current user
  - GET `/progress/{skill_id}`: Get progress for a specific skill
  - POST `/progress/`: Create a new progress entry
  - PATCH `/progress/{skill_id}`: Update progress for a skill
