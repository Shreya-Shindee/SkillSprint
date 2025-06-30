# SkillSprint Demo Setup 🚀

## Quick Start Guide

### Demo User Credentials

Use these credentials to test the login functionality:

#### 1. Main Demo User
- **Email:** demo@skillsprint.com
- **Username:** demo
- **Password:** demo123
- **XP:** 1250+

#### 2. Advanced User (Sarah)
- **Email:** sarah.demo@skillsprint.com
- **Username:** sarah_demo
- **Password:** sarah123
- **XP:** 2450+

#### 3. Beginner User (Alex)
- **Email:** alex.demo@skillsprint.com
- **Username:** alex_demo
- **Password:** alex123
- **XP:** 750+

#### 4. Admin User
- **Email:** admin@skillsprint.com
- **Username:** admin
- **Password:** admin123
- **XP:** 5000+

## How to Start Demo

### Option 1: Quick Start (Recommended)
```bash
cd backend
python start_demo.py
```

### Option 2: Manual Start
```bash
# Start Backend
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Start Frontend (in a new terminal)
cd frontend
npm start
```

## URLs
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs

## Demo Features
✅ Complete authentication system (Sign In/Register)  
✅ Beautiful landing page with interactive features  
✅ Dashboard with progress tracking  
✅ Learning paths and skill management  
✅ XP system and gamification  
✅ Resource recommendations  
✅ Responsive, modern UI design  

## Testing Tips
1. Start with the **demo** user for a balanced experience
2. Use **sarah_demo** to see advanced progress states
3. Use **alex_demo** for beginner-level testing
4. Use **admin** for administrative features

---
*Happy testing! 🎯*
