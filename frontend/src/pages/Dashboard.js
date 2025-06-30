import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { getAllSkills, getUserXP, getCurrentUser, getAllProgress, updateProgress, getDashboardStats, getAchievements, getActivityFeed, getInsights, decomposeSkill } from '../api';
import { useToast } from '../contexts/ToastContext';
import SkillCard from '../components/SkillCard';
import SkillCarousel from '../components/SkillCarousel';
import InProgressCarousel from '../components/InProgressCarousel';
import XPBar from '../components/XPBar';
import LoadingSpinner from '../components/LoadingSpinner';
import ProgressBar from '../components/ProgressBar';
import PageTransition from '../components/PageTransition';
import LearningPathCard from '../components/LearningPathCard';

const Dashboard = () => {
  const navigate = useNavigate();
  const { addToast } = useToast();
  
  const [skills, setSkills] = useState([]);
  const [xp, setXP] = useState(0);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [skillInput, setSkillInput] = useState('');
  // Store progress data for future use
  const [progressData, setProgressData] = useState([]);
  // Store recent activity for future use
  const [recentActivity, setRecentActivity] = useState([]);
  const [skillsInProgress, setSkillsInProgress] = useState([]);
  const [completedSkills, setCompletedSkills] = useState([]);
  const [subskillsByMain, setSubskillsByMain] = useState({});
  const [completedSubskillsByMain, setCompletedSubskillsByMain] = useState({});
  const [currentDate] = useState(new Date());
  
  // New state for enhanced features
  const [dashboardStats, setDashboardStats] = useState(null);
  const [achievements, setAchievements] = useState([]);
  const [leaderboard, setLeaderboard] = useState([]);
  const [activityFeed, setActivityFeed] = useState([]);
  const [progressChart, setProgressChart] = useState(null);
  const [insights, setInsights] = useState(null);
  const [activeTab, setActiveTab] = useState('overview');

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        // Fetch all required data
        const [userResponse, skillsResponse, xpResponse, progressResponse] = await Promise.all([
          getCurrentUser(),
          getAllSkills(),
          getUserXP(),
          getAllProgress()
        ]);
        
        setUser(userResponse.data);
        setSkills(skillsResponse.data);
        setXP(xpResponse.data);
        
        // Process progress data
        if (progressResponse.data) {
          setProgressData(progressResponse.data);
          
          // Create recent activity from progress data (last 5 items)
          const activity = [...progressResponse.data]
            .sort((a, b) => new Date(b.updated_at) - new Date(a.updated_at))
            .slice(0, 5);

          // Only include main skills (parent_id == null) that have at least one incomplete subskill
          const mainSkills = skillsResponse.data.filter(s => !s.parent_id);
          // Identify skills in progress and completed skills
          let inProgress = [];
          let completed = [];
          // Build a map of skillId to progress
          let progressMap = {};
          for (const progress of progressResponse.data) {
            progressMap[progress.skill_id] = progress;
          }
          for (const mainSkill of mainSkills) {
            // Find subskills for this main skill
            const subskills = skillsResponse.data.filter(s => s.parent_id === mainSkill.id);
            // If there are no subskills, treat the main skill's own progress
            if (subskills.length === 0) {
              const mainProgress = progressMap[mainSkill.id];
              if (mainProgress && !mainProgress.completed) {
                inProgress.push({ ...mainSkill, progress: mainProgress.progress_percentage });
              } else if (mainProgress && mainProgress.completed) {
                completed.push({ ...mainSkill, progress: mainProgress.progress_percentage });
              }
            } else {
              // If any subskill is not completed, show the main skill as in progress
              const incompleteSubskills = subskills.filter(sub => {
                const subProgress = progressMap[sub.id];
                return subProgress && !subProgress.completed;
              });
              if (incompleteSubskills.length > 0) {
                // Optionally, calculate overall progress as average of subskills
                const total = subskills.length;
                const completedCount = subskills.filter(sub => {
                  const subProgress = progressMap[sub.id];
                  return subProgress && subProgress.completed;
                }).length;
                const percent = total > 0 ? Math.round((completedCount / total) * 100) : 0;
                inProgress.push({ ...mainSkill, progress: percent });
              } else {
                // All subskills completed, mark main skill as completed
                completed.push({ ...mainSkill, progress: 100 });
              }
            }
          }

          setSkillsInProgress(inProgress);
          setCompletedSkills(completed);
          setRecentActivity(activity);

          // Build subskills and completion status for each main skill in progress
          const subskillsMap = {};
          const completedMap = {};
          for (const mainSkill of inProgress) {
            const subskills = skillsResponse.data.filter(s => s.parent_id === mainSkill.id);
            subskillsMap[mainSkill.id] = subskills;
            const completedSet = new Set();
            for (const sub of subskills) {
              const subProgress = progressResponse.data.find(p => p.skill_id === sub.id);
              if (subProgress && subProgress.completed) {
                completedSet.add(sub.name);
              }
            }
            completedMap[mainSkill.id] = completedSet;
          }
          setSubskillsByMain(subskillsMap);
          setCompletedSubskillsByMain(completedMap);
        }
      } catch (error) {
        console.error('Error fetching dashboard data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
    // Listen for streakUpdated event to refresh dashboard
    const handleStreakUpdate = () => {
      fetchData();
    };
    window.addEventListener('streakUpdated', handleStreakUpdate);
    return () => {
      window.removeEventListener('streakUpdated', handleStreakUpdate);
    };
  }, []);

  // Enhanced data fetching functions
  const fetchDashboardStats = async () => {
    try {
      const response = await getDashboardStats();
      if (response.data) {
        setDashboardStats(response.data);
      }
    } catch (error) {
      console.error('Error fetching dashboard stats:', error);
    }
  };

  const fetchAchievements = async () => {
    try {
      const response = await getAchievements();
      if (response.data) {
        setAchievements(response.data);
      }
    } catch (error) {
      console.error('Error fetching achievements:', error);
    }
  };

  const fetchActivityFeed = async () => {
    try {
      const response = await getActivityFeed();
      if (response.data) {
        setActivityFeed(response.data.activities || []);
      }
    } catch (error) {
      console.error('Error fetching activity feed:', error);
    }
  };

  const fetchInsights = async () => {
    try {
      const response = await getInsights();
      if (response.data) {
        setInsights(response.data);
      }
    } catch (error) {
      console.error('Error fetching insights:', error);
    }
  };

  // Calculate XP for next level
  const nextLevelXP = Math.ceil(xp / 1000) * 1000;
  
  // Format date to display
  const formattedDate = currentDate.toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });

  const handleCreatePath = async () => {
    if (skillInput.trim()) {
      try {
        const skillNameLower = skillInput.trim().toLowerCase();
        
        // Check if this skill is already in progress
        const existingSkill = skillsInProgress.find(skill => 
          skill.name.toLowerCase().includes(skillNameLower) || 
          skillNameLower.includes(skill.name.toLowerCase())
        );
        
        if (existingSkill) {
          // If skill already exists, navigate to continue learning
          addToast(`Continuing your ${existingSkill.name} learning path!`, 'info');
          navigate(`/learning-path/${existingSkill.id}`);
          return;
        }
        
        // Check if skill is completed
        const completedSkill = completedSkills.find(skill => 
          skill.name.toLowerCase().includes(skillNameLower) || 
          skillNameLower.includes(skill.name.toLowerCase())
        );
        
        if (completedSkill) {
          addToast(`You've already completed ${completedSkill.name}! Starting a review session.`, 'success');
          navigate(`/learning-path/${completedSkill.id}`);
          return;
        }
        
        // First try to decompose the skill and get the learning path
        const response = await decomposeSkill(skillInput.trim());
        if (response.data && response.data.skill_id) {
          // Navigate to the learning path with the actual skill ID
          addToast(`Created new learning path for ${skillInput.trim()}!`, 'success');
          navigate(`/learning-path/${response.data.skill_id}`);
        } else {
          // Fallback to skill name if no ID is returned
          navigate(`/learning-path/${encodeURIComponent(skillInput.trim())}`);
        }
      } catch (error) {
        console.error('Error creating learning path:', error);
        addToast('Failed to create learning path. Please try again.', 'error');
      }
    }
  };

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      handleCreatePath();
    }
  };

  // Helper function to determine button text and state based on skill input
  const getButtonState = () => {
    if (!skillInput.trim()) {
      return {
        text: 'Create',
        title: 'Please enter a skill name first',
        disabled: true,
        className: 'bg-gray-400 cursor-not-allowed'
      };
    }

    const skillNameLower = skillInput.trim().toLowerCase();
    
    // Check if skill is in progress
    const existingSkill = skillsInProgress.find(skill => 
      skill.name.toLowerCase().includes(skillNameLower) || 
      skillNameLower.includes(skill.name.toLowerCase())
    );
    
    if (existingSkill) {
      return {
        text: 'Continue',
        title: `Continue learning ${existingSkill.name}`,
        disabled: false,
        className: 'bg-green-600 hover:bg-green-700 cursor-pointer hover:shadow-lg transform hover:scale-105'
      };
    }
    
    // Check if skill is completed
    const completedSkill = completedSkills.find(skill => 
      skill.name.toLowerCase().includes(skillNameLower) || 
      skillNameLower.includes(skill.name.toLowerCase())
    );
    
    if (completedSkill) {
      return {
        text: 'Review',
        title: `Review ${completedSkill.name} (already completed)`,
        disabled: false,
        className: 'bg-blue-600 hover:bg-blue-700 cursor-pointer hover:shadow-lg transform hover:scale-105'
      };
    }
    
    // New skill
    return {
      text: 'Create',
      title: 'Create your learning path now!',
      disabled: false,
      className: 'bg-indigo-600 hover:bg-indigo-700 cursor-pointer hover:shadow-lg transform hover:scale-105'
    };
  };

  const buttonState = getButtonState();

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-indigo-50 to-blue-50">
        <div className="text-center">
          <LoadingSpinner />
          <p className="mt-4 text-indigo-600 font-medium animate-pulse">Loading your learning dashboard...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="pt-20 pb-12 px-4 bg-gradient-to-br from-gray-50 to-slate-100 min-h-screen">
      <div className="max-w-7xl mx-auto">
        {/* Personalized Welcome Message */}
        <div className="bg-white shadow-lg rounded-2xl p-8 mb-8 border border-gray-100 relative overflow-hidden">
          {/* Decorative elements */}
          <div className="absolute top-0 right-0 w-64 h-64 bg-gradient-to-br from-indigo-200 to-purple-200 rounded-full -mr-32 -mt-32 opacity-20"></div>
          <div className="absolute bottom-0 left-0 w-64 h-64 bg-gradient-to-tr from-blue-200 to-cyan-200 rounded-full -ml-32 -mb-32 opacity-20"></div>
          
          <div className="relative z-10">
            <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
              <div>
                <h1 className="text-3xl md:text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 mb-2">
                  Welcome back, {user?.username || 'Learner'}!
                </h1>
                <p className="text-gray-600 flex items-center">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                  {formattedDate}
                </p>
              </div>
              
              <div className="bg-gradient-to-r from-indigo-50 to-purple-50 p-4 rounded-xl border border-indigo-100 shadow-sm">
                <p className="text-gray-700 font-medium">Ready to continue your learning journey?</p>
                <Link to={skillsInProgress.length > 0 ? `/skills/${skillsInProgress[0].id}` : '/dashboard'} 
                  className="mt-2 inline-flex items-center font-medium text-indigo-600 hover:text-indigo-500 group">
                  Resume learning
                  <svg xmlns="http://www.w3.org/2000/svg" className="ml-1 h-5 w-5 transform transition-transform group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                  </svg>
                </Link>
              </div>
            </div>
          </div>
        </div>

        {/* XP Progress */}
        <div className="mb-8">
          <XPBar currentXP={xp} nextLevelXP={nextLevelXP} />
        </div>

        {/* Progress Overview */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8 border border-gray-100">
          <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 mr-2 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            Progress Overview
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-gradient-to-br from-indigo-50 to-blue-50 rounded-xl p-6 border border-indigo-100 shadow-sm hover:shadow-md transition-shadow duration-300">
              <div className="flex items-start">
                <div className="p-3 bg-indigo-100 rounded-lg mr-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                </div>
                <div>
                  <h3 className="font-medium text-gray-700 text-lg mb-1">Skills In Progress</h3>
                  <p className="text-3xl font-bold text-indigo-700">{skillsInProgress.length}</p>
                </div>
              </div>
            </div>
            
            <div className="bg-gradient-to-br from-emerald-50 to-green-50 rounded-xl p-6 border border-emerald-100 shadow-sm hover:shadow-md transition-shadow duration-300">
              <div className="flex items-start">
                <div className="p-3 bg-emerald-100 rounded-lg mr-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div>
                  <h3 className="font-medium text-gray-700 text-lg mb-1">Skills Completed</h3>
                  <p className="text-3xl font-bold text-emerald-700">{completedSkills.length}</p>
                </div>
              </div>
            </div>
            
            <div className="bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl p-6 border border-purple-100 shadow-sm hover:shadow-md transition-shadow duration-300">
              <div className="flex items-start">
                <div className="p-3 bg-purple-100 rounded-lg mr-4">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8 text-purple-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div>
                  <h3 className="font-medium text-gray-700 text-lg mb-1">Total XP Earned</h3>
                  <p className="text-3xl font-bold text-purple-700">{xp}</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Content Sections */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
          {/* Continue Learning */}
          <div data-section="continue-learning" className="bg-white rounded-2xl shadow-lg p-8 border border-gray-100 h-full scroll-mt-20">
            <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 mr-2 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
              Continue Learning
            </h2>
            <InProgressCarousel 
              skills={skillsInProgress} 
              onSkillRemove={(skillId) => {
                setSkillsInProgress(prev => prev.filter(s => s.id !== skillId));
              }}
            />
          </div>

          {/* Create Custom Path */}
          <div id="create-path" className="bg-white rounded-2xl shadow-lg p-8 border border-gray-100 h-full scroll-mt-20">
            <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 mr-2 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
              </svg>
              Create Custom Learning Path
            </h2>
            
            <div className="bg-gradient-to-r from-indigo-50 to-blue-50 rounded-xl p-6 mb-6 border border-indigo-100">
              <h3 className="font-semibold text-gray-800 mb-2">AI-Powered Learning Paths</h3>
              <p className="text-gray-600 mb-4">
                Enter any skill you want to learn, and our AI will generate a personalized step-by-step learning path tailored just for you.
              </p>
              
              <div className="relative group">
                <input
                  type="text"
                  placeholder="e.g. Machine Learning, Web Development, Digital Marketing..."
                  value={skillInput}
                  onChange={(e) => setSkillInput(e.target.value)}
                  onKeyPress={handleKeyPress}
                  className="w-full px-4 py-3 pr-24 border border-indigo-200 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all duration-300 focus:shadow-lg"
                />
                {!skillInput.trim() && (
                  <div className="absolute -top-12 left-0 bg-indigo-600 text-white px-3 py-2 rounded-lg text-sm opacity-0 group-focus-within:opacity-100 transition-opacity duration-300 whitespace-nowrap z-10">
                    💡 Start typing any skill you want to master!
                    <div className="absolute top-full left-4 w-0 h-0 border-l-4 border-r-4 border-t-4 border-transparent border-t-indigo-600"></div>
                  </div>
                )}
                {skillInput.trim() && buttonState.text === 'Continue' && (
                  <div className="absolute -top-12 left-0 bg-green-600 text-white px-3 py-2 rounded-lg text-sm opacity-0 group-focus-within:opacity-100 transition-opacity duration-300 whitespace-nowrap z-10">
                    🚀 Continue your existing learning path!
                    <div className="absolute top-full left-4 w-0 h-0 border-l-4 border-r-4 border-t-4 border-transparent border-t-green-600"></div>
                  </div>
                )}
                {skillInput.trim() && buttonState.text === 'Review' && (
                  <div className="absolute -top-12 left-0 bg-blue-600 text-white px-3 py-2 rounded-lg text-sm opacity-0 group-focus-within:opacity-100 transition-opacity duration-300 whitespace-nowrap z-10">
                    📚 Review your completed skill!
                    <div className="absolute top-full left-4 w-0 h-0 border-l-4 border-r-4 border-t-4 border-transparent border-t-blue-600"></div>
                  </div>
                )}
                <button
                  onClick={handleCreatePath}
                  disabled={buttonState.disabled}
                  title={buttonState.title}
                  className={`absolute right-2 top-2 px-4 py-1 rounded-lg text-white text-sm font-medium transition-all duration-300 ${buttonState.className}`}
                >
                  {buttonState.text}
                </button>
              </div>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="bg-amber-50 rounded-xl p-5 border border-amber-100 shadow-sm">
                <div className="flex items-center mb-2">
                  <div className="w-10 h-10 rounded-full bg-amber-100 flex items-center justify-center mr-3">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                    </svg>
                  </div>
                  <h3 className="font-semibold text-gray-800">Discover New Skills</h3>
                </div>
                <p className="text-gray-600 text-sm">
                  Explore trending skills in tech, business, creativity and more.
                </p>
              </div>
              
              <div className="bg-emerald-50 rounded-xl p-5 border border-emerald-100 shadow-sm">
                <div className="flex items-center mb-2">
                  <div className="w-10 h-10 rounded-full bg-emerald-100 flex items-center justify-center mr-3">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                    </svg>
                  </div>
                  <h3 className="font-semibold text-gray-800">Personalized Plans</h3>
                </div>
                <p className="text-gray-600 text-sm">
                  Get learning paths tailored to your specific goals and experience level.
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Popular Skills */}
        <SkillCarousel 
          skills={skills.filter(skill => !skill.parent_id)} 
          title="Popular Skills"
          showViewAll={true}
        />
      </div>
    </div>
  );
};

export default Dashboard;
