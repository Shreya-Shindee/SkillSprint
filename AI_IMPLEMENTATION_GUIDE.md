# SkillSprint - AI-Powered Adaptive Learning Platform

## 🚀 Project Overview

SkillSprint is a comprehensive educational learning platform that adapts dynamically to learner needs. It features AI-powered skill decomposition, adaptive quiz generation, collaborative filtering recommendations, and gamified progress tracking.

## ✨ Key Features Implemented

### Stage 1: MVP (Smart Static Adaptive System) ✅
- ✅ **AI-Powered Skill Decomposition**: Uses LLM (Gemini/OpenAI) to break down skills into subskills
- ✅ **Dynamic Learning Path Generation**: Creates personalized roadmaps based on user level
- ✅ **Adaptive Quiz System**: AI-generated quiz questions with difficulty adjustment
- ✅ **Gamified Dashboard**: XP system, streaks, achievements, and leaderboards
- ✅ **Progress Tracking**: Granular subskill tracking with time monitoring
- ✅ **Authentication**: JWT-based secure user authentication

### Stage 2: Data-Driven Adaptive Learning ✅
- ✅ **User Behavior Tracking**: Comprehensive logging of learning activities
- ✅ **Collaborative Filtering**: Recommendations based on similar learners
- ✅ **Dynamic Difficulty Adjustment**: Automatic content difficulty based on performance
- ✅ **Learning Analytics**: Detailed insights into learning patterns
- ✅ **Enhanced Dashboard**: Visual analytics, heatmaps, progress charts

### Stage 3: AI-Based Path Generation & Resource Optimization ✅
- ✅ **LLM-Based Roadmap Generator**: GPT/Gemini integration for personalized paths
- ✅ **Intelligent Resource Matching**: AI-powered resource recommendations
- ✅ **Automated Quiz Generation**: LLM-generated MCQs with explanations
- ✅ **Behavioral Learning Insights**: AI analysis of learning preferences

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI with Python 3.8+
- **Database**: SQLite with SQLAlchemy ORM
- **AI/ML**: 
  - Sentence Transformers for embeddings
  - OpenAI API / Google Gemini for LLM features
  - Scikit-learn for collaborative filtering
- **Authentication**: JWT tokens with bcrypt hashing

### Frontend
- **Framework**: React.js with modern hooks
- **Styling**: TailwindCSS for responsive design
- **State Management**: React Context API
- **Routing**: React Router for SPA navigation

### AI Integration
- **LLM Providers**: OpenAI GPT-3.5/4, Google Gemini
- **ML Models**: SentenceTransformers, collaborative filtering
- **Data Analysis**: Pandas, NumPy for user behavior analysis

## � Quick Start

### Automated Setup (Recommended)
```powershell
# Run the automated setup script
.\fast-start.ps1
```

This will:
- ✅ Check Python and Node.js installation
- ✅ Set up backend virtual environment
- ✅ Install all dependencies
- ✅ Initialize database
- ✅ Start both servers

### Manual Setup
See `QUICK_START.md` for detailed manual setup instructions.

### Health Check
```powershell
# Verify system health
python health_check.py
```

## 🔧 Installation & Setup

### 1. Environment Configuration

**Backend (.env):**
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

**Frontend (.env.development):**
```env
REACT_APP_API_URL=http://localhost:8000
REACT_APP_ENV=development
REACT_APP_DEBUG=true
REACT_APP_ENABLE_AI_FEATURES=true
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Initialize database
python -c "from database.init_db import init_database; init_database()"

# Start the FastAPI server
python main.py
```

The backend will be available at `http://localhost:8000`

### 3. Frontend Setup

```bash
# Navigate to frontend directory (from project root)
cd frontend

# Install dependencies
npm install

# Start the React development server
npm start
```

The frontend will be available at `http://localhost:3000`

## 🔑 API Keys Setup (Optional but Recommended)

To enable full AI features, set up API keys:

### For OpenAI (GPT-3.5/4):
1. Visit https://platform.openai.com/
2. Create an account and get your API key
3. Add to `.env` file: `OPENAI_API_KEY=your_key_here`

### For Google Gemini:
1. Visit https://makersuite.google.com/
2. Get your API key
3. Add to `.env` file: `GEMINI_API_KEY=your_key_here`

**Note**: The platform works without API keys using fallback methods, but AI features will be limited.

## 🎮 How to Use

### 1. User Registration/Login
1. Visit `http://localhost:3000`
2. Create a new account or login
3. Access the dashboard

### 2. Create a Learning Path
1. Click "Start New Skill" on dashboard
2. Enter a skill name (e.g., "Machine Learning", "React Development")
3. Choose your experience level and preferences
4. Let AI generate a personalized learning path

### 3. Follow Your Learning Journey
1. Navigate through subskills in order
2. Complete each subskill to earn XP
3. Take adaptive quizzes to test knowledge
4. Track progress and maintain streaks

### 4. Explore AI Features
1. **AI Insights**: View personalized learning recommendations
2. **Adaptive Quizzes**: Take quizzes that adjust to your level
3. **Smart Recommendations**: Discover skills similar users have completed
4. **Progress Analytics**: View detailed learning statistics

## 📊 Key Features Walkthrough

### AI-Powered Skill Creation
- Use the AI Skill Creator at `/skills/new`
- Input any skill name and get AI-generated subskills
- Personalized based on your level and learning style

### Adaptive Learning Engine
- System tracks your behavior and performance
- Automatically adjusts difficulty based on quiz scores
- Recommends next steps based on progress patterns

### Gamification System
- **XP Points**: Earn points for completing subskills and quizzes
- **Streaks**: Maintain daily learning streaks for bonuses
- **Achievements**: Unlock badges for milestones
- **Leaderboard**: Compete with other learners

### Analytics Dashboard
- View learning patterns and preferences
- Track time spent on different topics
- Get AI-powered insights for improvement

## 🔄 API Endpoints

### Core Endpoints
- `GET /` - API health check
- `POST /auth/register` - User registration
- `POST /auth/login` - User login

### Skills Management
- `POST /skills/decompose` - AI skill decomposition
- `POST /skills/ai-generate` - Full AI skill generation
- `GET /skills/{skill_id}/personalized-path` - Get personalized path
- `GET /skills/{skill_id}/analytics` - Skill analytics

### Quiz System
- `POST /quiz/generate` - Generate adaptive quiz
- `POST /quiz/submit` - Submit quiz answers
- `GET /quiz/history/{skill_id}` - Quiz history
- `GET /quiz/analytics/{skill_id}` - Quiz analytics

### Progress Tracking
- `POST /progress/subskill/complete` - Mark subskill complete
- `GET /progress/skill/{skill_id}` - Get skill progress
- `GET /progress/analytics` - Progress analytics

### Dashboard & Gamification
- `GET /dashboard/stats` - User statistics
- `GET /dashboard/achievements` - User achievements
- `GET /dashboard/leaderboard` - XP leaderboard
- `GET /dashboard/learning-insights` - AI insights

## 🧪 Demo Data

The system includes demo data with:
- Sample skills (Data Science, Web Development, AI)
- Pre-generated subskills and learning paths
- Sample quiz questions
- Demo user accounts

## 🔧 Customization

### Adding New LLM Providers
1. Extend `LLMIntegration` class in `utils/llm_integration.py`
2. Add new provider methods
3. Update environment variable handling

### Modifying Gamification Rules
1. Edit XP calculations in `utils/quiz_generator.py`
2. Adjust achievement definitions in `routers/dashboard.py`
3. Customize streak logic in `routers/progress.py`

### Enhancing Adaptive Learning
1. Modify behavior analysis in `utils/adaptive_learning.py`
2. Adjust difficulty calculation algorithms
3. Add new recommendation strategies

## 🚧 Future Enhancements (Stage 4)

### Planned Features
- **Reinforcement Learning Engine**: RL agent as intelligent tutor
- **Advanced Knowledge Graphs**: Neo4j integration for concept dependencies
- **Real-time Collaboration**: Multi-user learning sessions
- **Mobile App**: React Native mobile application
- **Advanced Analytics**: Machine learning for learning outcome prediction

## 🐛 Troubleshooting

### Common Issues

1. **Backend won't start**
   - Check Python version (3.8+ required)
   - Ensure virtual environment is activated
   - Verify all dependencies are installed

2. **Frontend won't connect to backend**
   - Ensure backend is running on port 3001
   - Check CORS settings in `main.py`
   - Verify API endpoints in frontend code

3. **AI features not working**
   - Check if API keys are set correctly
   - Verify internet connection for LLM calls
   - Fallback methods should work without API keys

4. **Database issues**
   - Delete `skillsprint.db` and run `init_db.py` again
   - Check file permissions in backend directory

### Getting Help
- Check console logs for error messages
- Review API response status codes
- Verify network requests in browser developer tools

## 📈 Performance Optimization

### Backend Optimizations
- Database query optimization with SQLAlchemy
- Caching for frequently accessed data
- Async endpoints for better concurrency

### Frontend Optimizations
- React.memo for component optimization
- Lazy loading for route components
- Efficient state management with Context API

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for GPT API
- Google for Gemini API
- Hugging Face for Sentence Transformers
- FastAPI and React communities for excellent frameworks

---

**Ready to revolutionize your learning experience? Start your SkillSprint journey today! 🚀**
