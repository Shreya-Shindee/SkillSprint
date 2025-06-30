# SkillSprint — AI-Powered Adaptive Learning Platform

SkillSprint is a comprehensive educational learning platform that adapts dynamically to learner needs. It features AI-powered skill decomposition, adaptive learning paths, quiz generation, gamified progress tracking, and collaborative filtering recommendations.

## 🚀 Quick Start

**Get started in 30 seconds:**

```powershell
# Clone the repository
git clone <repository-url>
cd SkillSprint

# Run automated setup
.\fast-start.ps1
```

Then visit:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000/docs

## ✨ Key Features

### Core Learning Platform
- 🎯 **AI-Powered Skill Decomposition**: Uses LLM to break down skills into subskills
- 📚 **Dynamic Learning Path Generation**: Creates personalized roadmaps
- 🧩 **Adaptive Quiz System**: AI-generated quiz questions with difficulty adjustment
- 📊 **Progress Tracking**: Granular subskill tracking with analytics
- 🏆 **Gamification System**: XP, achievements, streaks, and leaderboards

### AI-Enhanced Features
- 🤖 **LLM Integration**: OpenAI GPT and Google Gemini for content generation
- 🎲 **Collaborative Filtering**: Recommendations based on similar learners
- 📈 **Dynamic Difficulty Adjustment**: Automatic content difficulty based on performance
- 💡 **Behavioral Learning Insights**: AI analysis of learning preferences

### Modern Tech Stack
- **Backend**: FastAPI, SQLAlchemy, SQLite/PostgreSQL
- **Frontend**: React.js, TailwindCSS, Chart.js
- **AI/ML**: Sentence Transformers, OpenAI API, Gemini API
- **Authentication**: JWT tokens with bcrypt hashing

## 📋 Prerequisites

- **Python 3.8+** - [Download Python](https://python.org/downloads/)
- **Node.js 16+** - [Download Node.js](https://nodejs.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)

## 🛠️ Manual Setup

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\Activate.ps1  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python -c "from database.init_db import init_database; init_database()"
```

5. Start the backend server:
```bash
python main.py
```

The API will be available at http://localhost:8000 and documentation at http://localhost:8000/docs.

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will be available at http://localhost:3000.

## 🎮 Using the Application

1. **Register/Login**: Create an account to get started
2. **Explore Dashboard**: View your learning analytics and progress
3. **Create Skills**: Use the AI Skill Creator to generate learning paths
4. **Take Quizzes**: Test your knowledge with adaptive quizzes
5. **Track Progress**: Monitor your XP, achievements, and streaks
6. **Get Recommendations**: Receive personalized learning suggestions

## 📁 Project Structure

```
SkillSprint/
├── backend/          # FastAPI backend
│   ├── app/         # Application routers
│   ├── database/    # Database configuration
│   ├── models/      # SQLAlchemy models
│   ├── utils/       # AI integration & utilities
│   └── main.py      # Application entry point
├── frontend/         # React frontend
│   ├── src/
│   │   ├── pages/   # Main page components
│   │   ├── components/ # Reusable components
│   │   └── api/     # API client
│   └── public/      # Static assets
├── ml/              # Machine learning modules
├── fast-start.ps1   # Automated setup script
└── health_check.py  # System health verification
```

## 🔧 Configuration

### Environment Variables

**Backend (.env):**
- `PORT`: Server port (default: 8000)
- `SECRET_KEY`: JWT secret key
- `OPENAI_API_KEY`: OpenAI API key (optional)
- `GOOGLE_API_KEY`: Google Gemini API key (optional)

**Frontend (.env.development):**
- `REACT_APP_API_URL`: Backend API URL
- `REACT_APP_ENABLE_AI_FEATURES`: Enable AI features

### AI Integration (Optional)

To enable AI features, add your API keys to `backend/.env`:
```env
OPENAI_API_KEY=your-openai-api-key-here
GOOGLE_API_KEY=your-google-gemini-api-key-here
```

## 🚀 Production Deployment

```powershell
# Build for production
.\build-prod.ps1

# Deploy the dist folder
# Start production server
cd dist && .\start-production.ps1
```

## 🧪 Testing & Health Check

```powershell
# Run system health check
python health_check.py

# Backend tests
cd backend && python -m pytest

# Frontend tests
cd frontend && npm test
```

## 📚 Documentation

- **Quick Start**: `QUICK_START.md` - Fast setup guide
- **AI Implementation**: `AI_IMPLEMENTATION_GUIDE.md` - Technical details
- **Project Status**: `PROJECT_STATUS.md` - Implementation progress
- **API Docs**: Visit http://localhost:8000/docs when running

## 🎯 Development Stages

### Stage 1: MVP ✅ Complete
- User authentication and dashboard
- Skill management and learning paths
- Quiz system with scoring
- Basic progress tracking

### Stage 2: Data-Driven Learning ✅ Complete
- User behavior analytics
- Collaborative filtering recommendations
- Dynamic difficulty adjustment
- Enhanced dashboard with visualizations

### Stage 3: AI Integration ✅ Complete
- LLM-powered skill decomposition
- Automated quiz generation
- AI-driven learning path creation
- Behavioral learning insights

### Stage 4: RL Engine (Future)
- Reinforcement learning for optimization
- Advanced personalization algorithms
- Cognitive load modeling
- Real-time adaptation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**: Change ports in `.env` files
2. **Database issues**: Run `python health_check.py` to diagnose
3. **Module not found**: Ensure virtual environment is activated and dependencies installed
4. **API connection errors**: Verify backend is running on correct port

### Debug Commands

```powershell
# Check system health
python health_check.py

# Reset database
cd backend
python -c "from database.reset_db import reset_database; reset_database()"

# View API documentation
# Visit http://localhost:8000/docs
```

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- OpenAI for GPT API
- Google for Gemini API
- Sentence Transformers for embedding models
- React and FastAPI communities
- All contributors and testers

---

**Ready to start learning? Run `.\fast-start.ps1` and let SkillSprint adapt to your learning journey!** 🚀
