/**
 * Auto-login utility for local development
 * Automatically logs in with demo credentials when running locally
 */

import { loginUser } from '../api';

// Demo credentials for auto-login
const DEMO_CREDENTIALS = {
  username: 'testuser',
  password: 'password123'
};

// Check if we're in development mode and on localhost
const isLocalDevelopment = () => {
  return (
    process.env.NODE_ENV === 'development' ||
    window.location.hostname === 'localhost' ||
    window.location.hostname === '127.0.0.1'
  );
};

// Check if user is already logged in
const isLoggedIn = () => {
  const token = localStorage.getItem('token');
  return token && token !== 'null' && token !== 'undefined';
};

// Perform auto-login
const performAutoLogin = async () => {
  // Only auto-login in local development and if not already logged in
  if (!isLocalDevelopment() || isLoggedIn()) {
    return { success: false, reason: 'Not in dev mode or already logged in' };
  }

  try {
    console.log('🔄 Auto-login: Attempting to login with demo credentials...');
    
    const response = await loginUser(DEMO_CREDENTIALS.username, DEMO_CREDENTIALS.password);
    
    if (response.data && response.data.access_token) {
      // Store the token
      localStorage.setItem('token', response.data.access_token);
      localStorage.setItem('username', DEMO_CREDENTIALS.username);
      
      console.log('✅ Auto-login: Successfully logged in as', DEMO_CREDENTIALS.username);
      
      // Dispatch login event for other components
      window.dispatchEvent(new CustomEvent('autoLoginSuccess', {
        detail: { username: DEMO_CREDENTIALS.username }
      }));
      
      return { 
        success: true, 
        token: response.data.access_token,
        username: DEMO_CREDENTIALS.username
      };
    } else {
      console.error('❌ Auto-login: Invalid response format');
      return { success: false, reason: 'Invalid response format' };
    }
  } catch (error) {
    console.error('❌ Auto-login failed:', error.message);
    return { success: false, reason: error.message };
  }
};

// Check login status and auto-login if needed
const ensureLoggedIn = async () => {
  if (isLoggedIn()) {
    return { success: true, reason: 'Already logged in' };
  }
  
  return await performAutoLogin();
};

// Clear auto-login data (for manual logout)
const clearAutoLogin = () => {
  localStorage.removeItem('token');
  localStorage.removeItem('username');
  console.log('🔄 Auto-login: Cleared stored credentials');
};

// Create a default export object
const autoLoginUtils = {
  performAutoLogin,
  ensureLoggedIn,
  clearAutoLogin,
  isLocalDevelopment,
  isLoggedIn
};

// Named exports
export {
  performAutoLogin,
  ensureLoggedIn,
  clearAutoLogin,
  isLocalDevelopment,
  isLoggedIn
};

// Default export
export default autoLoginUtils;
