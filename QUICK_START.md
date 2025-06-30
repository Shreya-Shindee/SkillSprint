# SkillSprint - Quick Start Guide

## 🚀 Fast Development Setup

### Prerequisites
- **Python 3.8+** - [Download Python](https://python.org/downloads/)
- **Node.js 16+** - [Download Node.js](https://nodejs.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)

### Quick Start (Automated)

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd SkillSprint
   ```

2. **Run the fast setup script**:
   ```powershell
   .\fast-start.ps1
   ```

   This script will:
   - ✅ Check Python and Node.js installation
   - ✅ Create Python virtual environment
   - ✅ Install all backend dependencies
   - ✅ Initialize the database
   - ✅ Install all frontend dependencies
   - ✅ Start both backend and frontend servers

3. **Access the application**:
   - **Frontend**: http://localhost:3000
   - **Backend API**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs

### Manual Setup (Step by Step)

#### Backend Setup
```powershell
cd backend

# Create and activate virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Initialize database
python -c "from database.init_db import init_database; init_database()"

# Start backend server
python main.py
```

#### Frontend Setup
```powershell
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

## 🔧 Configuration

### Environment Variables

#### Backend (`.env`)
```env
# Server Configuration
PORT=8000
HOST=0.0.0.0
DEBUG=True

# Database
DATABASE_URL=sqlite:///./skillsprint.db

# JWT Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# AI Integration (Optional)
OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-google-gemini-api-key

# CORS
FRONTEND_URL=http://localhost:3000
```

#### Frontend (`.env.development`)
```env
# API Configuration
REACT_APP_API_URL=http://localhost:8000
REACT_APP_ENV=development
REACT_APP_DEBUG=true

# Feature Flags
REACT_APP_ENABLE_AI_FEATURES=true
REACT_APP_ENABLE_ANALYTICS=true
REACT_APP_ENABLE_GAMIFICATION=true
```

## 📱 Features Available

### Core Features (Working)
- ✅ **User Authentication** - Register, login, JWT tokens
- ✅ **Skill Management** - Create, view, and manage skills
- ✅ **Learning Paths** - Dynamic skill-based learning routes
- ✅ **Quiz System** - Interactive quizzes with scoring
- ✅ **Progress Tracking** - User progress monitoring
- ✅ **Dashboard** - User analytics and insights

### AI-Enhanced Features (Optional)
- 🤖 **AI Skill Decomposition** - Requires OpenAI/Gemini API key
- 🤖 **Adaptive Quiz Generation** - Requires OpenAI/Gemini API key
- 🤖 **Intelligent Recommendations** - Uses collaborative filtering
- 🤖 **Dynamic Difficulty Adjustment** - Based on user performance

### Gamification Features
- 🎮 **XP System** - Experience points for learning activities
- 🏆 **Achievements** - Unlock badges and milestones
- 📊 **Leaderboards** - Compare progress with other learners
- 🔥 **Streaks** - Daily learning streak tracking

## 🛠️ Development

### Project Structure
```
SkillSprint/
├── backend/          # FastAPI backend
│   ├── app/         # Application routers
│   ├── database/    # Database configuration
│   ├── models/      # SQLAlchemy models
│   ├── schemas/     # Pydantic schemas
│   ├── utils/       # Utility functions & AI integration
│   └── main.py      # Application entry point
├── frontend/         # React frontend
│   ├── src/
│   │   ├── components/ # Reusable components
│   │   ├── pages/     # Page components
│   │   ├── contexts/  # React contexts
│   │   └── api/       # API client
│   └── public/        # Static assets
└── ml/              # Machine learning modules
```

### Key Technologies
- **Backend**: FastAPI, SQLAlchemy, SQLite, JWT
- **Frontend**: React, TailwindCSS, Axios, Chart.js
- **AI/ML**: Sentence Transformers, OpenAI API, Gemini API
- **Database**: SQLite (development), PostgreSQL (production ready)

### Development Commands

#### Backend
```powershell
cd backend
venv\Scripts\Activate.ps1

# Run development server
python main.py

# Database operations
python -c "from database.init_db import init_database; init_database()"
python -c "from database.reset_db import reset_database; reset_database()"

# Run tests
python -m pytest

# Check API health
curl http://localhost:8000/health
```

#### Frontend
```powershell
cd frontend

# Development server
npm start

# Build for production
npm run build

# Run tests
npm test

# Lint code
npm run lint
```

## 🚀 Production Deployment

1. **Build for production**:
   ```powershell
   .\build-prod.ps1
   ```

2. **Deploy the `dist` folder** to your server

3. **Start production server**:
   ```powershell
   cd dist
   .\start-production.ps1
   ```

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**:
   ```powershell
   # Change ports in .env files
   # Backend: PORT=8001
   # Frontend: REACT_APP_API_URL=http://localhost:8001
   ```

2. **Database issues**:
   ```powershell
   cd backend
   python -c "from database.reset_db import reset_database; reset_database()"
   ```

3. **Module not found errors**:
   ```powershell
   cd backend
   venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

4. **Frontend build issues**:
   ```powershell
   cd frontend
   rm -rf node_modules
   npm install
   ```

### Debug Mode

Enable debug mode by setting:
- Backend: `DEBUG=True` in `.env`
- Frontend: `REACT_APP_DEBUG=true` in `.env.development`

### Logs

- **Backend logs**: Console output when running `python main.py`
- **Frontend logs**: Browser console (F12 → Console)
- **API logs**: Available at http://localhost:8000/docs

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the `AI_IMPLEMENTATION_GUIDE.md` for detailed technical information
3. Check the browser console and backend logs for error messages

## 🎯 Next Steps

After setup, try:
1. 📝 Register a new user account
2. 🎯 Create your first skill
3. 📚 Start a learning path
4. 🧩 Take a quiz
5. 📊 Check your dashboard progress
6. 🤖 Enable AI features with API keys (optional)
