import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { createProgress } from '../api';
import { useToast } from '../contexts/ToastContext';
import LoadingSpinner from '../components/LoadingSpinner';
import ProgressBar from '../components/ProgressBar';
import ResourceCard from '../components/ResourceCard';

const LearningPath = () => {
  const { skillId } = useParams();
  const navigate = useNavigate();
  const { addToast } = useToast();
  
  const [skill, setSkill] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [completedSubskills, setCompletedSubskills] = useState(new Set());
  const [loadingSubskill, setLoadingSubskill] = useState(null);
  const [resources, setResources] = useState({});
  const [loadingResources, setLoadingResources] = useState({});
  const [currentSubskill, setCurrentSubskill] = useState(null);
  const [showQuiz, setShowQuiz] = useState(false);
  const [quizQuestions, setQuizQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState('');
  const [score, setScore] = useState(0);
  const [quizCompleted, setQuizCompleted] = useState(false);
  const [quizResult, setQuizResult] = useState(null);
  const [quizStartTime, setQuizStartTime] = useState(0);
  const [progress, setProgress] = useState(0);
  const [hasStartedLearning, setHasStartedLearning] = useState(false);
  const [startingSkill, setStartingSkill] = useState(false);
  const [loadingQuiz, setLoadingQuiz] = useState(false);

  // Initialize resource cache from localStorage for persistence
  const initializeResourceCache = () => {
    try {
      const cached = localStorage.getItem(`skillsprint_resources_${skillId}`);
      if (cached) {
        const parsedCache = JSON.parse(cached);
        // Check if cache is less than 1 hour old
        const cacheTime = parsedCache.timestamp || 0;
        const now = Date.now();
        if (now - cacheTime < 3600000) { // 1 hour
          console.log('🚀 Loading resources from localStorage cache');
          return new Map(Object.entries(parsedCache.data || {}));
        }
      }
    } catch (error) {
      console.warn('Failed to load resource cache from localStorage:', error);
    }
    return new Map();
  };

  const [resourceCache, setResourceCache] = useState(initializeResourceCache);

  // Save resource cache to localStorage
  useEffect(() => {
    if (resourceCache.size > 0) {
      try {
        const cacheData = {
          timestamp: Date.now(),
          data: Object.fromEntries(resourceCache)
        };
        localStorage.setItem(`skillsprint_resources_${skillId}`, JSON.stringify(cacheData));
      } catch (error) {
        console.warn('Failed to save resource cache to localStorage:', error);
      }
    }
  }, [resourceCache, skillId]);

  useEffect(() => {
    fetchSkillDetails();
    fetchUserProgress();
  }, [skillId]);

  // Auto-fetch resources for all subskills when skill data is loaded
  useEffect(() => {
    if (skill && skill.subskills) {
      // Batch fetch all resources at once for better performance
      fetchAllResources(skill.subskills);
    }
  }, [skill]);

  // Update progress when completedSubskills or skill changes
  useEffect(() => {
    if (skill && skill.subskills) {
      const newProgress = (completedSubskills.size / skill.subskills.length) * 100;
      console.log('🔄 Progress Update:', {
        completedCount: completedSubskills.size,
        totalSubskills: skill.subskills.length,
        newProgress: newProgress,
        completedSubskills: Array.from(completedSubskills)
      });
      setProgress(newProgress);
    }
  }, [completedSubskills, skill]);

  // Fast URL validation - only check format and basic domain filtering
  const isValidResourceUrl = (url) => {
    try {
      const urlObj = new URL(url);
      
      // Filter out obviously invalid domains
      const invalidDomains = [
        'example.com',
        'test.com', 
        'localhost',
        '127.0.0.1',
        'placeholder.com',
        'dummy.com'
      ];
      
      if (invalidDomains.some(domain => urlObj.hostname.includes(domain))) {
        return false;
      }
      
      // Only allow HTTP/HTTPS URLs
      return ['http:', 'https:'].includes(urlObj.protocol);
    } catch {
      return false;
    }
  };

  // Fast resource filtering - only quality checks, no network validation
  const filterResources = (resources) => {
    if (!resources || resources.length === 0) return [];
    
    // Fast quality filtering without async validation
    const qualityFilteredResources = resources.filter(resource => {
      // Basic quality requirements
      if (!resource.title || resource.title.length < 10) return false;
      if (!resource.description || resource.description.length < 20) return false;
      if (!resource.url || !isValidResourceUrl(resource.url)) return false;
      
      // Filter out obvious placeholder content
      const lowQualityTerms = [
        'lorem ipsum',
        'placeholder', 
        'example',
        'test content',
        'dummy text',
        'sample data'
      ];
      
      const contentToCheck = `${resource.title} ${resource.description}`.toLowerCase();
      if (lowQualityTerms.some(term => contentToCheck.includes(term))) {
        return false;
      }
      
      return true;
    });
    
    // Prioritize high-quality domains
    const highQualityDomains = [
      'youtube.com',
      'youtu.be', 
      'coursera.org',
      'edx.org',
      'udemy.com',
      'khanacademy.org',
      'medium.com',
      'towardsdatascience.com',
      'github.com',
      'stackoverflow.com',
      'developer.mozilla.org',
      'w3schools.com',
      'freecodecamp.org',
      'codecademy.com',
      'pluralsight.com',
      'linkedin.com/learning',
      'docs.python.org',
      'pandas.pydata.org',
      'scikit-learn.org',
      'tensorflow.org',
      'pytorch.org',
      'kaggle.com',
      'datacamp.com'
    ];
    
    // Sort by priority and limit to top 4
    return qualityFilteredResources
      .map(resource => {
        try {
          const urlObj = new URL(resource.url);
          const isHighQuality = highQualityDomains.some(domain => 
            urlObj.hostname.includes(domain)
          );
          return { ...resource, priority: isHighQuality ? 1 : 2 };
        } catch {
          return { ...resource, priority: 3 };
        }
      })
      .sort((a, b) => a.priority - b.priority)
      .slice(0, 4);
  };

  const fetchAllResources = async (subskills) => {
    if (!subskills || subskills.length === 0) return;

    const token = localStorage.getItem('token');

    // Check cache first
    const uncachedSubskills = subskills.filter(subskill => !resourceCache.has(subskill));
    
    // If all subskills are cached, use cached data immediately
    if (uncachedSubskills.length === 0) {
      const cachedResources = {};
      subskills.forEach(subskill => {
        cachedResources[subskill] = resourceCache.get(subskill);
      });
      setResources(cachedResources);
      console.log(`⚡ Loaded ${subskills.length} subskills from cache instantly`);
      return;
    }

    console.log(`� Fast-loading resources for ${uncachedSubskills.length} new subskills`);

    try {
      // Mark as loading
      const loadingState = {};
      uncachedSubskills.forEach(subskill => {
        loadingState[subskill] = true;
      });
      setLoadingResources(prev => ({ ...prev, ...loadingState }));

      // Try batch endpoint first
      const response = await fetch('http://localhost:8000/resources/search/batch', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(uncachedSubskills)
      });

      if (response.ok) {
        const data = await response.json();
        
        // Fast processing without network validation
        const newResourceCache = new Map(resourceCache);
        const allResources = { ...resources };
        const loadingComplete = {};
        
        // Process and filter resources immediately (no async validation)
        uncachedSubskills.forEach(subskill => {
          const skillResources = data.results[subskill] || [];
          const filteredResources = filterResources(skillResources);
          
          newResourceCache.set(subskill, filteredResources);
          allResources[subskill] = filteredResources;
          loadingComplete[subskill] = false;
          
          console.log(`⚡ ${filteredResources.length} quality resources loaded for ${subskill}`);
        });

        // Add cached resources for other subskills
        subskills.forEach(subskill => {
          if (resourceCache.has(subskill)) {
            allResources[subskill] = resourceCache.get(subskill);
          }
        });

        setResourceCache(newResourceCache);
        setResources(allResources);
        setLoadingResources(prev => ({ ...prev, ...loadingComplete }));
        
        console.log(`✅ Fast-loaded resources for ${uncachedSubskills.length} subskills`);
      } else {
        throw new Error('Batch resource fetch failed');
      }
      
    } catch (error) {
      console.error('Batch fetch failed, using fallback:', error);
      
      // Fallback to individual requests
      const resourcePromises = uncachedSubskills.map(async (subskill) => {
        try {
          const response = await fetch(
            `http://localhost:8000/resources/search?skill=${encodeURIComponent(subskill)}&limit=6`, 
            {
              headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
              }
            }
          );

          if (response.ok) {
            const data = await response.json();
            const skillResources = data.resources || [];
            const filteredResources = filterResources(skillResources);
            return { subskill, resources: filteredResources };
          }
          return { subskill, resources: [] };
        } catch (error) {
          console.error(`Error fetching resources for ${subskill}:`, error);
          return { subskill, resources: [] };
        }
      });

      const results = await Promise.all(resourcePromises);
      
      // Update cache and state
      const newResourceCache = new Map(resourceCache);
      const allResources = { ...resources };
      const loadingComplete = {};
      
      results.forEach(({ subskill, resources: filteredResources }) => {
        newResourceCache.set(subskill, filteredResources);
        allResources[subskill] = filteredResources;
        loadingComplete[subskill] = false;
        console.log(`⚡ ${filteredResources.length} resources loaded for ${subskill} (fallback)`);
      });

      // Add cached resources
      subskills.forEach(subskill => {
        if (resourceCache.has(subskill)) {
          allResources[subskill] = resourceCache.get(subskill);
        }
      });

      setResourceCache(newResourceCache);
      setResources(allResources);
      setLoadingResources(prev => ({ ...prev, ...loadingComplete }));
    }
  };

  const fetchSkillDetails = async () => {
    try {
      setLoading(true);
      const token = localStorage.getItem('token');
      const response = await fetch(`http://localhost:8000/skills/${skillId}`, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      });

      if (!response.ok) {
        throw new Error('Failed to fetch skill details');
      }

      const data = await response.json();
      setSkill(data);
    } catch (err) {
      console.error('Error fetching skill details:', err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const fetchUserProgress = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch(`http://localhost:8000/progress/skill/${skillId}`, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        const progressData = await response.json();
        setCompletedSubskills(new Set(progressData.completed_subskills || []));
        // Use the has_started field from backend to determine if skill was started
        setHasStartedLearning(progressData.has_started || false);
      } else if (response.status === 404) {
        // Skill progress doesn't exist yet
        setHasStartedLearning(false);
      }
    } catch (err) {
      console.error('Error fetching user progress:', err);
      setHasStartedLearning(false);
    }
  };

  const toggleSubskillCompletion = async (subskillName) => {
    try {
      setLoadingSubskill(subskillName);
      const token = localStorage.getItem('token');
      const isCompleted = completedSubskills.has(subskillName);
      
      const endpoint = isCompleted ? 'uncomplete' : 'complete';
      const requestData = {
        skill_id: parseInt(skillId),
        subskill_name: subskillName,
        completed: !isCompleted,
        time_spent_minutes: 0
      };

      const response = await fetch(`http://localhost:8000/progress/subskill/${endpoint}`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ detail: 'Unknown error' }));
        throw new Error(errorData.detail || `Failed to ${isCompleted ? 'uncomplete' : 'complete'} subskill`);
      }

      const data = await response.json();
      
      // Update local state
      setCompletedSubskills(prev => {
        const newSet = new Set(prev);
        if (isCompleted) {
          newSet.delete(subskillName);
          console.log('❌ Removed subskill:', subskillName, 'New set size:', newSet.size);
        } else {
          newSet.add(subskillName);
          console.log('✅ Added subskill:', subskillName, 'New set size:', newSet.size);
        }
        console.log('📊 Updated completed subskills:', Array.from(newSet));
        return newSet;
      });

      // Dispatch custom event for dashboard updates only if we have response data
      if (data && !isCompleted) {
        window.dispatchEvent(new CustomEvent('streakUpdated', {
          detail: { 
            streak: data.current_streak || 0,
            xp: data.total_xp || 0,
            completedToday: data.completed_today || false
          }
        }));
      }

      addToast(
        isCompleted ? 'Subskill unmarked' : `Subskill completed! ${data.xp_earned ? `+${data.xp_earned} XP` : ''}`,
        isCompleted ? 'info' : 'success'
      );

    } catch (err) {
      console.error('Error toggling subskill completion:', err);
      addToast('Failed to update progress', 'error');
    } finally {
      setLoadingSubskill(null);
    }
  };

  const startQuiz = async () => {
    console.log('🎯🎯🎯 QUIZ BUTTON CLICKED - startQuiz function called');
    console.log('📋 Skill ID:', skillId);
    
    const token = localStorage.getItem('token');
    console.log('🔑 Token available:', !!token);
    console.log('🔑 Token preview:', token ? `${token.substring(0, 20)}...` : 'null');
    console.log('👤 Current loadingQuiz state:', loadingQuiz);
    console.log('👤 Current showQuiz state:', showQuiz);
    
    if (!token) {
      console.error('❌ No authentication token found');
      addToast('Please log in to take the quiz', 'error');
      navigate('/login');
      return;
    }
    
    setLoadingQuiz(true);
    
    try {
      console.log('📡 Making request to quiz API...');
      
      const response = await fetch(`http://localhost:8000/quiz/generate`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          skill_id: parseInt(skillId),
          num_questions: 5,
          difficulty: "adaptive"
        })
      });

      console.log('📡 Quiz API response status:', response.status);
      console.log('📡 Quiz API response headers:', Object.fromEntries(response.headers.entries()));

      if (response.ok) {
        const data = await response.json();
        console.log('📋 Quiz data received:', data);
        setQuizQuestions(data.questions || []);
        setShowQuiz(true);
        setCurrentQuestion(0);
        setScore(0);
        setQuizCompleted(false);
        setQuizStartTime(Date.now());
        console.log('✅ Quiz modal should now be visible, showQuiz set to true');
      } else if (response.status === 401) {
        console.error('❌ Authentication failed - token may be expired');
        const errorData = await response.json().catch(() => ({ detail: 'Authentication failed' }));
        console.error('❌ Error details:', errorData);
        
        // Clear invalid token and redirect to login
        localStorage.removeItem('token');
        addToast('Your session has expired. Please log in again.', 'error');
        navigate('/login');
      } else {
        const errorData = await response.json().catch(() => ({ detail: 'Unknown error' }));
        console.error('❌ Quiz API error:', response.status, errorData);
        addToast(`Failed to load quiz: ${errorData.detail || 'Unknown error'}`, 'error');
      }
    } catch (err) {
      console.error('💥 Error starting quiz:', err);
      addToast('Failed to load quiz. Please check your connection.', 'error');
    } finally {
      setLoadingQuiz(false);
      console.log('🏁 Quiz loading finished, loadingQuiz set to false');
    }
  };

  const submitQuizAnswer = () => {
    const isCorrect = selectedAnswer === quizQuestions[currentQuestion]?.correct_answer;
    if (isCorrect) {
      setScore(prev => prev + 1);
    }

    if (currentQuestion < quizQuestions.length - 1) {
      setCurrentQuestion(prev => prev + 1);
      setSelectedAnswer('');
    } else {
      // Submit complete quiz
      submitCompleteQuiz();
    }
  };

  const submitCompleteQuiz = async () => {
    try {
      const timeTaken = Math.floor((Date.now() - quizStartTime) / 1000);
      const token = localStorage.getItem('token');
      
      // Collect all user answers
      const userAnswers = quizQuestions.map((_, index) => {
        if (index === currentQuestion) {
          return selectedAnswer;
        }
        // This is simplified - in practice, you'd track all answers
        return "";
      });

      const response = await fetch(`http://localhost:8000/quiz/submit`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          skill_id: parseInt(skillId),
          questions: quizQuestions,
          user_answers: userAnswers,
          time_taken_seconds: timeTaken
        })
      });

      if (response.ok) {
        const result = await response.json();
        setQuizResult(result);
        setQuizCompleted(true);
        
        // Show XP gained
        if (result.xp_earned > 0) {
          addToast(`Quiz completed! +${result.xp_earned} XP`, 'success');
        }
        
        // Dispatch custom event for dashboard updates
        window.dispatchEvent(new CustomEvent('streakUpdated', {
          detail: { 
            xp: result.xp_earned || 0,
            completedToday: true
          }
        }));
      }
    } catch (err) {
      console.error('Error submitting quiz:', err);
      addToast('Failed to submit quiz', 'error');
    }
  };

  const closeQuiz = () => {
    setShowQuiz(false);
    setCurrentQuestion(0);
    setSelectedAnswer('');
    setScore(0);
    setQuizCompleted(false);
  };

  const startLearning = async () => {
    if (hasStartedLearning) return;
    
    try {
      setStartingSkill(true);
      
      const progressData = {
        skill_id: parseInt(skillId),
        progress_percentage: 0,
        completed: false
      };

      const response = await createProgress(progressData);
      
      if (response.data) {
        setHasStartedLearning(true);
        addToast('🎉 Started learning! +50 XP earned. This skill is now in your Continue Learning section.', 'success');
        
        // Dispatch custom event for dashboard updates
        window.dispatchEvent(new CustomEvent('streakUpdated', {
          detail: { 
            xp: 50,
            completedToday: false
          }
        }));
      }
    } catch (err) {
      console.error('Error starting skill:', err);
      if (err.response?.status === 400) {
        // Skill already started
        setHasStartedLearning(true);
        addToast('You have already started this skill!', 'info');
      } else {
        addToast('Failed to start learning. Please try again.', 'error');
      }
    } finally {
      setStartingSkill(false);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <LoadingSpinner />
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Error Loading Skill</h2>
          <p className="text-gray-600 mb-6">{error}</p>
          <button
            onClick={() => navigate('/dashboard')}
            className="bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700 transition-colors"
          >
            Back to Dashboard
          </button>
        </div>
      </div>
    );
  }

  if (!skill) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Skill Not Found</h2>
          <button
            onClick={() => navigate('/dashboard')}
            className="bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700 transition-colors"
          >
            Back to Dashboard
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 pt-16">
      {/* Quiz Modal */}
      {showQuiz && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-xl p-8 max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto">
            {!quizCompleted ? (
              <>
                <div className="flex justify-between items-center mb-6">
                  <h2 className="text-2xl font-bold text-gray-900">
                    Quiz: {skill.name}
                  </h2>
                  <button
                    onClick={closeQuiz}
                    className="text-gray-400 hover:text-gray-600"
                  >
                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>

                <div className="mb-6">
                  <div className="flex justify-between text-sm text-gray-500 mb-2">
                    <span>Question {currentQuestion + 1} of {quizQuestions.length}</span>
                    <span>Score: {score}/{quizQuestions.length}</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div
                      className="bg-indigo-600 h-2 rounded-full transition-all duration-300"
                      style={{ width: `${((currentQuestion + 1) / quizQuestions.length) * 100}%` }}
                    ></div>
                  </div>
                </div>

                {quizQuestions[currentQuestion] && (
                  <div>
                    <h3 className="text-lg font-semibold text-gray-900 mb-4">
                      {quizQuestions[currentQuestion].question}
                    </h3>

                    <div className="space-y-3 mb-6">
                      {quizQuestions[currentQuestion].options?.map((option, index) => (
                        <label
                          key={index}
                          className={`flex items-center p-3 border rounded-lg cursor-pointer transition-colors ${
                            selectedAnswer === option
                              ? 'bg-indigo-50 border-indigo-500'
                              : 'border-gray-200 hover:bg-gray-50'
                          }`}
                        >
                          <input
                            type="radio"
                            name="answer"
                            value={option}
                            checked={selectedAnswer === option}
                            onChange={(e) => setSelectedAnswer(e.target.value)}
                            className="sr-only"
                          />
                          <div className={`w-4 h-4 rounded-full border-2 mr-3 ${
                            selectedAnswer === option
                              ? 'bg-indigo-600 border-indigo-600'
                              : 'border-gray-300'
                          }`}>
                            {selectedAnswer === option && (
                              <div className="w-2 h-2 bg-white rounded-full m-0.5"></div>
                            )}
                          </div>
                          {option}
                        </label>
                      ))}
                    </div>

                    <button
                      onClick={submitQuizAnswer}
                      disabled={!selectedAnswer}
                      className="w-full bg-indigo-600 text-white py-3 px-6 rounded-lg hover:bg-indigo-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors"
                    >
                      {currentQuestion < quizQuestions.length - 1 ? 'Next Question' : 'Finish Quiz'}
                    </button>
                  </div>
                )}
              </>
            ) : (
              <div className="text-center">
                <div className="mb-6">
                  <div className="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                    <svg className="w-10 h-10 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <h2 className="text-2xl font-bold text-gray-900 mb-2">Quiz Completed!</h2>
                  <p className="text-gray-600 mb-4">
                    You scored {score} out of {quizQuestions.length} questions correctly.
                  </p>
                  <div className="text-3xl font-bold text-indigo-600 mb-2">
                    {Math.round((score / quizQuestions.length) * 100)}%
                  </div>
                  
                  {/* Enhanced results with XP and performance level */}
                  {quizResult && (
                    <div className="bg-gray-50 rounded-lg p-4 mb-4">
                      <div className="grid grid-cols-2 gap-4 text-sm">
                        <div>
                          <span className="text-gray-600">Performance:</span>
                          <span className="ml-2 font-semibold text-indigo-600">
                            {quizResult.performance_level}
                          </span>
                        </div>
                        <div>
                          <span className="text-gray-600">XP Earned:</span>
                          <span className="ml-2 font-semibold text-green-600">
                            +{quizResult.xp_earned}
                          </span>
                        </div>
                        <div>
                          <span className="text-gray-600">Time Taken:</span>
                          <span className="ml-2 font-semibold">
                            {Math.floor(quizResult.time_taken_seconds / 60)}m {quizResult.time_taken_seconds % 60}s
                          </span>
                        </div>
                        <div>
                          <span className="text-gray-600">Accuracy:</span>
                          <span className="ml-2 font-semibold">
                            {quizResult.score_percentage.toFixed(1)}%
                          </span>
                        </div>
                      </div>
                    </div>
                  )}

                  {/* Recommendations */}
                  {quizResult && quizResult.recommendations && quizResult.recommendations.length > 0 && (
                    <div className="bg-blue-50 rounded-lg p-4 mb-6">
                      <h3 className="font-semibold text-blue-900 mb-2">Recommendations:</h3>
                      <ul className="text-sm text-blue-800 space-y-1">
                        {quizResult.recommendations.map((rec, index) => (
                          <li key={index} className="flex items-start">
                            <span className="text-blue-600 mr-2">•</span>
                            {rec}
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>

                <button
                  onClick={closeQuiz}
                  className="bg-indigo-600 text-white py-3 px-6 rounded-lg hover:bg-indigo-700 transition-colors"
                >
                  Close Quiz
                </button>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Header */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3">
          {/* Back Button */}
          <div className="mb-3">
            <button
              onClick={() => navigate('/dashboard')}
              className="flex items-center text-gray-600 hover:text-gray-900 transition-colors"
            >
              <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
              Back to Dashboard
            </button>
          </div>
        </div>
      </div>

      {/* Title and Description Section - Higher positioning */}
      <div className="bg-white -mt-6">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center pt-2 pb-1">
            <h1 className="text-2xl md:text-3xl font-bold text-gray-900 mb-2">{skill.name}</h1>
            <p className="text-gray-600 text-base max-w-2xl mx-auto">{skill.description}</p>
          </div>
        </div>
      </div>

      {/* Progress and Actions Section - Compact */}
      <div className="bg-white border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          {/* Progress Bar */}
          <div className="mb-3">
            <div className="flex justify-between items-center text-sm text-gray-600 mb-2">
              <div className="flex items-center">
                <span>Progress</span>
                {hasStartedLearning && (
                  <span className="ml-2 inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium bg-indigo-100 text-indigo-800">
                    <svg className="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                    In Progress
                  </span>
                )}
              </div>
              <span>{completedSubskills.size} of {skill.subskills?.length || 0} completed</span>
            </div>
            <ProgressBar percentage={progress} className="h-2" />
          </div>

          {/* Compact Status and Actions */}
          <div className="flex flex-col space-y-3">
            {/* Status Message for Started Skills */}
            {hasStartedLearning && (
              <div className="text-sm text-gray-600">
                <span>
                  Learning in progress • Check{' '}
                  <button
                    onClick={() => {
                      navigate('/dashboard');
                      setTimeout(() => {
                        const continueElement = document.querySelector('[data-section="continue-learning"]');
                        if (continueElement) {
                          continueElement.scrollIntoView({ 
                            behavior: 'smooth',
                            block: 'start'
                          });
                        }
                      }, 100);
                    }}
                    className="text-indigo-600 hover:text-indigo-800 underline font-semibold"
                  >
                    Continue Learning
                  </button>
                  {' '}for progress tracking
                </span>
              </div>
            )}

            {/* Action Buttons - Stacked on small screens, horizontal on larger */}
            <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
              {/* Start Learning Button - Only show if not started */}
              {!hasStartedLearning && (
                <button
                  onClick={startLearning}
                  disabled={startingSkill}
                  className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-6 py-2.5 rounded-lg hover:from-indigo-700 hover:to-purple-700 transition-all duration-300 font-medium shadow-md flex items-center justify-center text-sm disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {startingSkill ? (
                    <>
                      <div className="w-4 h-4 mr-2 animate-spin rounded-full border-2 border-white border-t-transparent"></div>
                      Starting...
                    </>
                  ) : (
                    <>
                      <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                      </svg>
                      Start Learning
                    </>
                  )}
                </button>
              )}

              {/* Already Started Message - Show if already started */}
              {hasStartedLearning && (
                <div className="bg-gradient-to-r from-green-50 to-emerald-50 border border-green-200 rounded-lg px-4 py-2 flex items-center justify-center space-x-2">
                  <svg className="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <span className="text-green-800 font-medium text-sm">
                    Already started!
                  </span>
                </div>
              )}
              
              {/* Take Quiz Button */}
              <button
                onClick={startQuiz}
                disabled={loadingQuiz}
                className="bg-gradient-to-r from-green-600 to-emerald-600 text-white px-6 py-2.5 rounded-lg hover:from-green-700 hover:to-emerald-700 transition-all duration-300 font-medium shadow-md flex items-center justify-center text-sm disabled:opacity-50 disabled:cursor-not-allowed"
                style={{ zIndex: 1 }}
              >
                {loadingQuiz ? (
                  <>
                    <div className="w-4 h-4 mr-2 animate-spin rounded-full border-2 border-white border-t-transparent"></div>
                    Loading Quiz...
                  </>
                ) : (
                  <>
                    <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    Take Quiz
                  </>
                )}
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="w-full">
          {/* Subskills List */}
          <div className="w-full">
            <h2 className="text-2xl font-bold text-gray-900 mb-6">Learning Path</h2>
            <div className="space-y-6">
              {skill.subskills?.map((subskill, index) => {
                const isCompleted = completedSubskills.has(subskill);
                const isLoading = loadingSubskill === subskill;

                return (
                  <div
                    key={subskill}
                    className={`border rounded-xl p-6 transition-all duration-300 transform hover:scale-[1.02] hover:shadow-lg ${
                      isCompleted
                        ? 'bg-green-50 border-green-200 hover:bg-green-100'
                        : 'bg-white border-gray-200 hover:border-indigo-300 hover:bg-gray-50'
                    }`}
                  >
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center mb-3">
                          <div className={`w-8 h-8 rounded-full flex items-center justify-center text-white font-bold mr-3 ${
                            isCompleted ? 'bg-green-500' : 'bg-gray-400'
                          }`}>
                            {index + 1}
                          </div>
                          <h3 className="text-lg font-semibold text-gray-900">{subskill}</h3>
                        </div>

                        {/* Resources */}
                        <div className="ml-11">
                          {loadingResources[subskill] && (
                            <div className="flex items-center text-gray-500 text-sm mb-3">
                              <LoadingSpinner size="small" />
                              <span className="ml-2">Loading resources...</span>
                            </div>
                          )}

                          {resources[subskill] && resources[subskill].length > 0 && (
                            <div className="mb-3">
                              <h4 className="text-sm font-medium text-gray-700 mb-2 flex items-center">
                                <svg className="w-4 h-4 mr-1 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                                </svg>
                                Learning Resources
                              </h4>
                              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                {resources[subskill].map((resource, idx) => (
                                  <ResourceCard key={idx} resource={resource} />
                                ))}
                              </div>
                            </div>
                          )}

                          {!loadingResources[subskill] && (!resources[subskill] || resources[subskill].length === 0) && (
                            <div className="text-sm text-gray-500 italic mb-3">
                              No resources found for this subskill.
                            </div>
                          )}
                        </div>
                      </div>

                      <button
                        onClick={() => toggleSubskillCompletion(subskill)}
                        disabled={isLoading}
                        className={`ml-4 px-4 py-2 rounded-lg font-medium transition-all duration-300 ${
                          isCompleted
                            ? 'bg-green-100 text-green-700 hover:bg-green-200'
                            : 'bg-indigo-600 text-white hover:bg-indigo-700'
                        } ${isLoading ? 'opacity-50 cursor-not-allowed' : ''}`}
                      >
                        {isLoading ? (
                          <LoadingSpinner size="small" />
                        ) : isCompleted ? (
                          'Completed'
                        ) : (
                          'Mark Complete'
                        )}
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LearningPath;
