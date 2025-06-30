import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import { ToastProvider } from './contexts/ToastContext';

// Pages
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import Register from './pages/Register';
import SkillDetail from './pages/SkillDetail';
import LearningPath from './pages/LearningPath';
import Profile from './pages/Profile';
import NotFound from './pages/NotFound';
import LandingPage from './pages/LandingPage';
import Onboarding from './pages/Onboarding';

// Components
import Navbar from './components/Navbar';
import LoadingSpinner from './components/LoadingSpinner';
import './App.css';

// Protected route component
const ProtectedRoute = ({ children }) => {
  const { currentUser, loading } = useAuth();
  
  if (loading) {
    return <LoadingSpinner />;
  }
  
  if (!currentUser) {
    return <Navigate to="/login" />;
  }
  
  return children;
};

// Dashboard route with onboarding check
const DashboardRoute = () => {
  const [isOnboardingComplete, setIsOnboardingComplete] = useState(
    localStorage.getItem('onboardingComplete') === 'true'
  );
  
  // Listen for localStorage changes
  useEffect(() => {
    const handleStorageChange = () => {
      setIsOnboardingComplete(localStorage.getItem('onboardingComplete') === 'true');
    };
    
    window.addEventListener('storage', handleStorageChange);
    
    // Also check on component mount
    const checkOnboarding = () => {
      setIsOnboardingComplete(localStorage.getItem('onboardingComplete') === 'true');
    };
    
    checkOnboarding();
    
    return () => {
      window.removeEventListener('storage', handleStorageChange);
    };
  }, []);
  
  return (
    <ProtectedRoute>
      {isOnboardingComplete ? <Dashboard /> : <Navigate to="/onboarding" replace />}
    </ProtectedRoute>
  );
};

function App() {

  return (
    <AuthProvider>
      <ToastProvider>
        <Router>
          <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100">
            <Navbar />
            <div className="relative">
              {/* Decorative background elements */}
              <div className="fixed top-20 left-10 w-64 h-64 bg-indigo-500 rounded-full mix-blend-multiply filter blur-3xl opacity-5 animate-float"></div>
              <div className="fixed top-40 right-10 w-80 h-80 bg-blue-500 rounded-full mix-blend-multiply filter blur-3xl opacity-5 animate-float delay-200"></div>
              <div className="fixed bottom-20 left-40 w-72 h-72 bg-purple-500 rounded-full mix-blend-multiply filter blur-3xl opacity-5 animate-float delay-300"></div>
              
              <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/dashboard" element={<DashboardRoute />} />
                <Route path="/skills/:skillId" element={
                  <ProtectedRoute>
                    <SkillDetail />
                  </ProtectedRoute>
                } />
                <Route path="/learning-path/:skillId" element={
                  <ProtectedRoute>
                    <LearningPath />
                  </ProtectedRoute>
                } />
                <Route path="/profile" element={
                  <ProtectedRoute>
                    <Profile />
                  </ProtectedRoute>
                } />
                <Route path="/" element={<LandingPage />} />
                <Route path="/onboarding" element={<Onboarding />} />
                <Route path="*" element={<NotFound />} />
              </Routes>
            </div>
          </div>
        </Router>
      </ToastProvider>
    </AuthProvider>
  );
}

export default App;
