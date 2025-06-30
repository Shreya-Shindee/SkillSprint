import axios from 'axios';

// Create API client with environment variable support
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

console.log('API_URL:', API_URL);
console.log('Environment:', process.env.REACT_APP_ENV || 'development');

const api = axios.create({
  baseURL: API_URL,
  timeout: 30000, // Increased timeout for resource generation
});

// Add interceptor for JWT token
api.interceptors.request.use(
  (config) => {
    console.log(`Making ${config.method.toUpperCase()} request to: ${config.baseURL}${config.url}`);
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    console.error('Request error:', error);
    return Promise.reject(error);
  }
);

// Add response interceptor for debugging
api.interceptors.response.use(
  (response) => {
    console.log(`Response from ${response.config.url}:`, response.status);
    return response;
  },
  (error) => {
    console.error('API Error:', error.message);
    if (error.response) {
      console.error('Error data:', error.response.data);
      console.error('Error status:', error.response.status);
    } else if (error.request) {
      console.error('No response received:', error.request);
    }
    return Promise.reject(error);
  }
);

// Auth API
export const registerUser = (userData) => api.post('/auth/register', userData);
export const loginUser = (username, password) => {
  const formData = new FormData();
  formData.append('username', username);
  formData.append('password', password);
  return api.post('/auth/token', formData);
};

// User API
export const getCurrentUser = () => api.get('/users/me');
export const getUserXP = () => api.get('/users/xp');
export const getXPHistory = () => api.get('/users/xp/history');

// Skills API
export const getAllSkills = () => api.get('/skills');
export const getSkill = (skillId) => api.get(`/skills/${skillId}`);
export const createSkill = (skillData) => api.post('/skills', skillData);
export const decomposeSkill = (skillName) => {
  console.log('decomposeSkill called with:', skillName);
  return api.post('/skills/decompose', { skill_name: skillName });
};
export const getLearningPath = (skillName) => {
  console.log('getLearningPath called with:', skillName);
  return api.post('/skills/learning-path', { skill_name: skillName });
};

// Resources API
export const getAllResources = () => api.get('/resources');
export const getResource = (resourceId) => api.get(`/resources/${resourceId}`);
export const getResourcesBySkill = (skillId) => api.get(`/resources/skill/${skillId}`);
export const getResourcesBySkillName = (skillName) => {
  console.log('getResourcesBySkillName called with:', skillName);
  return api.post('/resources/by-skill-name', { skill_name: skillName });
};
export const createResource = (resourceData) => api.post('/resources', resourceData);

// Progress API
export const getAllProgress = () => api.get('/progress');
export const getSkillProgress = (skillId) => api.get(`/progress/${skillId}`);
export const createProgress = (progressData) => api.post('/progress', progressData);
export const updateProgress = (skillId, progressData) => api.patch(`/progress/${skillId}`, progressData);

// Dashboard API
export const getDashboardStats = () => api.get('/dashboard/stats');
export const getAchievements = () => api.get('/dashboard/achievements');
export const getLeaderboard = () => api.get('/dashboard/leaderboard');
export const getActivityFeed = () => api.get('/dashboard/activity');
export const getProgressChart = () => api.get('/dashboard/progress-chart');
export const getInsights = () => api.get('/dashboard/insights');

export default api;
