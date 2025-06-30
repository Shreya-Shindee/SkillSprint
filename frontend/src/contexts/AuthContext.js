import React, { createContext, useState, useEffect, useContext } from 'react';
import { loginUser, registerUser, getCurrentUser } from '../api';
import { performAutoLogin, isLocalDevelopment } from '../utils/autoLogin';

// Create Auth Context
const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Check if user is already logged in on page load
  useEffect(() => {
    const initializeAuth = async () => {
      const token = localStorage.getItem('token');
      
      if (token) {
        // User has token, fetch current user
        await fetchCurrentUser();
      } else if (isLocalDevelopment()) {
        // No token but in dev mode, attempt auto-login
        console.log('🔄 Development mode detected, attempting auto-login...');
        const autoLoginResult = await performAutoLogin();
        
        if (autoLoginResult.success) {
          // Auto-login successful, fetch user data
          await fetchCurrentUser();
        } else {
          console.log('🔄 Auto-login skipped:', autoLoginResult.reason);
          setLoading(false);
        }
      } else {
        // Production mode, no auto-login
        setLoading(false);
      }
    };

    initializeAuth();
  }, []);

  // Fetch current user data
  const fetchCurrentUser = async () => {
    try {
      setLoading(true);
      const { data } = await getCurrentUser();
      setCurrentUser(data);
      setError(null);
    } catch (err) {
      console.error('Error fetching user:', err);
      setError('Failed to authenticate user');
      localStorage.removeItem('token');
    } finally {
      setLoading(false);
    }
  };

  // Login function
  const login = async (username, password) => {
    try {
      setLoading(true);
      const { data } = await loginUser(username, password);
      localStorage.setItem('token', data.access_token);
      await fetchCurrentUser();
      return true;
    } catch (err) {
      console.error('Login error:', err);
      setError(err.response?.data?.detail || 'Failed to login');
      return false;
    } finally {
      setLoading(false);
    }
  };
  // Register function
  const register = async (userData) => {
    try {
      setLoading(true);
      console.log('Registration data:', userData);
      const response = await registerUser(userData);
      console.log('Registration response:', response);
      
      // If successful, proceed to login
      const success = await login(userData.username, userData.password);
      return success;
    } catch (err) {
      console.error('Registration error:', err);
      // More detailed error message for better debugging
      if (err.response) {
        console.error('Error response data:', err.response.data);
        console.error('Error response status:', err.response.status);
        setError(err.response?.data?.detail || `Failed to register (${err.response.status})`);
      } else if (err.request) {
        console.error('No response received:', err.request);
        setError('No response from server. Check if backend is running.');
      } else {
        console.error('Error setting up request:', err.message);
        setError(`Error: ${err.message}`);
      }
      return false;
    } finally {
      setLoading(false);
    }
  };

  // Logout function
  const logout = () => {
    localStorage.removeItem('token');
    setCurrentUser(null);
  };

  // Context value
  const value = {
    currentUser,
    loading,
    error,
    login,
    register,
    logout,
    isAuthenticated: !!currentUser,
    refreshUser: fetchCurrentUser,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

// Custom hook to use auth context
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export default AuthContext;
