import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { getLearningPath, decomposeSkill, createSkill, getResourcesBySkillName, createProgress, getAllSkills, getAllProgress, updateProgress } from '../api';
import { useAuth } from '../contexts/AuthContext';
import { useToast } from '../contexts/ToastContext';
import LoadingSpinner from '../components/LoadingSpinner';
import ResourceCard from '../components/ResourceCard';
import QuizComponent from '../components/QuizComponent';

const LearningPath = () => {
  const { skillName } = useParams();
  const navigate = useNavigate();
  const { currentUser, refreshUser } = useAuth();
  const { success } = useToast();
  const [path, setPath] = useState([]);
  const [skillTree, setSkillTree] = useState(null);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);
  const [resources, setResources] = useState({});
  const [loadingResources, setLoadingResources] = useState({});
  const [showQuiz, setShowQuiz] = useState(false);
  const [currentQuizSkill, setCurrentQuizSkill] = useState({ skillName: '', subskillName: '' });
  const [completedSubskills, setCompletedSubskills] = useState(new Set());
  const [mainSkillId, setMainSkillId] = useState(null);
  const [subskillsData, setSubskillsData] = useState({});
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        
        // Decode the URL parameter and capitalize first letter of each word
        const decodedSkillName = decodeURIComponent(skillName);
        const formattedSkillName = decodedSkillName
          .split(' ')
          .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
          .join(' ');
          
        console.log("Original skill name from URL:", skillName);
        console.log("Decoded skill name:", decodedSkillName);
        console.log("Formatted skill name:", formattedSkillName);
        
        // Get learning path using formatted skill name
        console.log("Calling getLearningPath API");
        const pathResponse = await getLearningPath(formattedSkillName);
        console.log("Learning path response:", pathResponse);
        setPath(pathResponse.data);
        
        // Get skill tree structure
        console.log("Calling decomposeSkill API");
        const treeResponse = await decomposeSkill(formattedSkillName);
        console.log("Skill tree response:", treeResponse);
        setSkillTree(treeResponse.data);
        
        // Get resources for each skill in the path
        const skills = [formattedSkillName, ...pathResponse.data.filter(s => s !== formattedSkillName)];
        
        // List of skills that have fast fallback resources (no loading needed)
        const fastFallbackSkills = [
          'Python', 'JavaScript', 'Variables', 'Data Types', 'Control Flow', 
          'Functions', 'OOP', 'Machine Learning', 'Deep Learning', 'Data Science',
          'Algorithms', 'Data Structures', 'Web Development', 'DevOps',
          'Python Fundamentals', 'Python Intermediate Concepts', 'Python Advanced Topics'
        ];
        
        // Fetch resources for all skills in the path with optimized loading states
        const resourcePromises = skills.map(async (skill) => {
          try {
            // Only show loading for skills that don't have fast fallback
            const hasFastFallback = fastFallbackSkills.includes(skill);
            if (!hasFastFallback) {
              setLoadingResources(prev => ({ ...prev, [skill]: true }));
            }
            
            console.log(`Fetching resources for ${skill}${hasFastFallback ? ' (fast fallback available)' : ''}`);
            const resourceResponse = await getResourcesBySkillName(skill);
            console.log(`Resources for ${skill}:`, resourceResponse.data);
            
            // Ensure we have at least some resources for each skill
            const skillResources = resourceResponse.data[skill] || [];
            if (skillResources.length === 0) {
              console.warn(`No resources found for ${skill}, this should not happen with our fallback system`);
            }
            
            setResources(prev => ({ 
              ...prev, 
              [skill]: skillResources 
            }));
            
            return { skill, success: true, resources: skillResources };
          } catch (resourceErr) {
            console.error(`Error fetching resources for ${skill}:`, resourceErr);
            
            // Set empty array for failed resource fetch - our backend should handle this
            setResources(prev => ({ 
              ...prev, 
              [skill]: [] 
            }));
            
            return { skill, success: false, error: resourceErr };
          } finally {
            setLoadingResources(prev => ({ ...prev, [skill]: false }));
          }
        });
        
        // Wait for all resource fetches to complete
        const resourceResults = await Promise.allSettled(resourcePromises);
        console.log('Resource fetch results:', resourceResults);
        
      } catch (err) {
        console.error('Error fetching learning path:', err);
        console.error('Error details:', err.response?.data || err.message);
        setError('Failed to generate learning path');
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, [skillName]);

  // Load existing skill data and completion status
  useEffect(() => {
    const loadExistingSkillData = async () => {
      if (!skillTree) return;
      
      try {
        const allSkillsResponse = await getAllSkills();
        const formattedSkillName = skillTree.name;
        
        // Check if the main skill already exists
        const existingMainSkill = allSkillsResponse.data.find(
          skill => skill.name.toLowerCase() === formattedSkillName.toLowerCase()
        );
        
        if (existingMainSkill) {
          setMainSkillId(existingMainSkill.id);
          // Load completion status for existing skill
          await loadSubskillCompletionStatus(existingMainSkill.id, allSkillsResponse.data);
        }
      } catch (error) {
        console.error('Error loading existing skill data:', error);
      }
    };

    loadExistingSkillData();
  }, [skillTree]);

  const handleStartQuiz = (skillName, subskillName) => {
    setCurrentQuizSkill({ skillName, subskillName });
    setShowQuiz(true);
  };

  const handleQuizComplete = async (result) => {
    console.log('Quiz completed:', result);
    // Refresh user data to update XP everywhere
    if (refreshUser) {
      await refreshUser();
    }
    setShowQuiz(false);
    // You could add a toast notification here
  };

  const handleCloseQuiz = () => {
    setShowQuiz(false);
    setCurrentQuizSkill({ skillName: '', subskillName: '' });
  };

  // Load existing completion status for subskills
  const loadSubskillCompletionStatus = async (skillId = mainSkillId, allSkills = null) => {
    try {
      if (!skillId) return;
      
      const allSkillsResponse = allSkills ? { data: allSkills } : await getAllSkills();
      const allProgressResponse = await getAllProgress();
      
      // Find all subskills for this main skill
      const subskills = allSkillsResponse.data.filter(skill => skill.parent_id === skillId);
      const completed = new Set();
      
      // Create a mapping of subskill names to their data
      const subskillMapping = {};
      subskills.forEach(subskill => {
        subskillMapping[subskill.name] = subskill;
        
        // Check if this subskill has progress marked as completed
        const progress = allProgressResponse.data.find(p => p.skill_id === subskill.id);
        if (progress && progress.completed) {
          completed.add(subskill.name);
        }
      });
      
      setSubskillsData(subskillMapping);
      setCompletedSubskills(completed);
    } catch (error) {
      console.error('Error loading subskill completion status:', error);
    }
  };

  // Handle marking a subskill as complete
  const handleMarkSubskillComplete = async (subskillName) => {
    try {
      const subskill = subskillsData[subskillName];
      if (!subskill) return;

      // Update the subskill progress to completed
      await updateProgress(subskill.id, {
        progress_percentage: 100,
        completed: true
      });

      // Update local state
      const newCompleted = new Set(completedSubskills);
      newCompleted.add(subskillName);
      setCompletedSubskills(newCompleted);

      // Calculate overall progress for the main skill
      const totalSubskills = path.length;
      const completedCount = newCompleted.size;
      const overallProgress = Math.round((completedCount / totalSubskills) * 100);

      // Update main skill progress
      if (mainSkillId) {
        await updateProgress(mainSkillId, {
          progress_percentage: overallProgress,
          completed: overallProgress === 100
        });
      }

      success(`${subskillName} marked as complete! (${completedCount}/${totalSubskills} completed)`);
      
      // Trigger global progress update
      window.dispatchEvent(new Event('streakUpdated'));
      
    } catch (error) {
      console.error('Error marking subskill as complete:', error);
    }
  };

  // Handle unmarking a subskill (toggle functionality)
  const handleUnmarkSubskillComplete = async (subskillName) => {
    try {
      const subskill = subskillsData[subskillName];
      if (!subskill) return;

      // Update the subskill progress to not completed
      await updateProgress(subskill.id, {
        progress_percentage: 0,
        completed: false
      });

      // Update local state
      const newCompleted = new Set(completedSubskills);
      newCompleted.delete(subskillName);
      setCompletedSubskills(newCompleted);

      // Calculate overall progress for the main skill
      const totalSubskills = path.length;
      const completedCount = newCompleted.size;
      const overallProgress = Math.round((completedCount / totalSubskills) * 100);

      // Update main skill progress
      if (mainSkillId) {
        await updateProgress(mainSkillId, {
          progress_percentage: overallProgress,
          completed: false
        });
      }

      success(`${subskillName} unmarked. Progress updated.`);
      
      // Trigger global progress update
      window.dispatchEvent(new Event('streakUpdated'));
      
    } catch (error) {
      console.error('Error unmarking subskill:', error);
    }
  };

  const handleSavePath = async () => {
    try {
      setSaving(true);
      
      // Check if the skill already exists
      console.log("Checking if skill exists...");
      const allSkillsResponse = await getAllSkills();
      const existingSkill = allSkillsResponse.data.find(
        skill => skill.name.toLowerCase() === skillTree.name.toLowerCase()
      );
      
      let mainSkillId;
      
      if (existingSkill) {
        console.log("Skill already exists, using existing skill:", existingSkill);
        mainSkillId = existingSkill.id;
      } else {
        // Create main skill if it doesn't exist
        const mainSkill = {
          name: skillTree.name,
          description: `Learning path for ${skillTree.name}`
        };
        
        const mainSkillResponse = await createSkill(mainSkill);
        mainSkillId = mainSkillResponse.data.id;
      }
      
      // Create subskills with parent relationship
      const createSubskillPromises = skillTree.children.map(async (child) => {
        // Check if this subskill already exists with the same parent
        const existingSubskill = allSkillsResponse.data.find(
          skill => skill.name.toLowerCase() === child.name.toLowerCase() && 
                  skill.parent_id === mainSkillId
        );
        
        if (existingSubskill) {
          console.log(`Subskill ${child.name} already exists with parent ID ${mainSkillId}, using existing:`, existingSubskill);
          return existingSubskill;
        } else {
          // Create new subskill
          const newSubskill = await createSkill({
            name: child.name,
            description: `Subskill of ${skillTree.name}`,
            parent_id: mainSkillId
          });
          return newSubskill.data;
        }
      });
      
      // Execute all promises and store the results for potential future use
      await Promise.all(createSubskillPromises);
      
      // Check if progress already exists for the main skill
      try {
        // Get all progress to check if we already have progress for this skill
        const allProgressResponse = await getAllProgress();
        const existingProgress = allProgressResponse.data.find(
          progress => progress.skill_id === mainSkillId
        );
        
        if (!existingProgress) {
          // Create progress for the main skill (initiate at 0%) only if it doesn't exist
          const progressData = {
            skill_id: mainSkillId,
            progress_percentage: 0,
            completed: false
          };
          
          await createProgress(progressData);
          console.log("Created initial progress for main skill");
        } else {
          console.log("Progress already exists for this skill:", existingProgress);
        }
      } catch (progressErr) {
        console.error("Error with progress:", progressErr);
        // Continue with navigation even if progress creation fails
      }

      // Store the main skill ID and load completion status
      setMainSkillId(mainSkillId);
      
      // Navigate to the main skill
      navigate(`/skills/${mainSkillId}`);
      
    } catch (err) {
      console.error('Error saving learning path:', err);
      setError('Failed to save learning path');
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return <LoadingSpinner />;
  }

  if (error) {
    return (
      <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
        {error}
      </div>
    );
  }

  return (
    <div className="bg-gradient-to-br from-gray-50 to-gray-100 min-h-screen p-6">
      <div className="max-w-6xl mx-auto">
        <div className="mb-8 bg-white bg-opacity-70 backdrop-blur-sm p-8 rounded-2xl shadow-lg">
          <div className="flex items-center mb-4">
            <Link to="/dashboard" className="text-indigo-600 hover:text-indigo-800 font-medium mr-2 transition-colors duration-300 flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M9.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L7.414 9H15a1 1 0 110 2H7.414l2.293 2.293a1 1 0 010 1.414z" clipRule="evenodd" />
              </svg>
              Dashboard
            </Link>
            <span className="text-gray-400 mx-2">|</span>
            <span className="text-gray-700 font-medium">Learning Path</span>
          </div>
          <div className="relative">
            <div className="absolute inset-0 bg-gradient-to-r from-purple-500 to-indigo-600 rounded-xl opacity-10"></div>
            <div className="relative p-6">
              <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-indigo-700 mb-3">
                {skillName} Learning Journey
              </h1>
              <p className="text-gray-600 text-lg">Follow this AI-crafted roadmap to master {skillName}</p>
            </div>
          </div>
        </div>

        {/* Learning Path Visualization */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8 transition-all duration-300 hover:shadow-xl">
          <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-8 border-b border-gray-100 pb-6">
            <h2 className="text-2xl font-bold text-gray-800 flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-indigo-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
              Your Learning Sequence
            </h2>
            <button
              onClick={handleSavePath}
              disabled={saving}
              className={`${saving ? 'bg-gray-400' : 'bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700'} 
                text-white px-6 py-3 rounded-full font-medium flex items-center transition-all duration-300 transform hover:scale-105 shadow-md`}
            >
              {saving ? (
                <>
                  <LoadingSpinner size="small" /> 
                  <span className="ml-2">Saving...</span>
                </>
              ) : (
                <>
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M7.707 10.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V6h5a2 2 0 012 2v7a2 2 0 01-2 2H4a2 2 0 01-2-2V8a2 2 0 012-2h5v5.586l-1.293-1.293zM9 4a1 1 0 012 0v2H9V4z" />
                  </svg>
                  Start This Learning Journey
                </>
              )}
            </button>
          </div>

          {/* Progress Overview */}
          {path.length > 0 && (
            <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-6 mb-6 border border-blue-200">
              <div className="flex items-center justify-between mb-3">
                <h3 className="text-lg font-semibold text-gray-800">Learning Progress</h3>
                <span className="text-sm font-medium text-indigo-600">
                  {completedSubskills.size} of {path.length} completed
                </span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-3 mb-2">
                <div 
                  className="bg-gradient-to-r from-green-500 to-emerald-600 h-3 rounded-full transition-all duration-500 ease-out"
                  style={{ width: `${path.length > 0 ? (completedSubskills.size / path.length) * 100 : 0}%` }}
                ></div>
              </div>
              <p className="text-sm text-gray-600">
                {completedSubskills.size === path.length ? 
                  "🎉 Congratulations! You've completed all subskills in this learning path!" :
                  `Keep going! ${path.length - completedSubskills.size} more ${path.length - completedSubskills.size === 1 ? 'step' : 'steps'} to complete.`
                }
              </p>
            </div>
          )}
      
          <div className="space-y-6">
            {path.map((step, index) => {
              const isCompleted = completedSubskills.has(step);
              return (
                <div key={index} className="flex items-start w-full">
                  <div className={`flex items-center justify-center w-10 h-10 rounded-full 
                    ${isCompleted ? 'bg-gradient-to-r from-green-500 to-emerald-600' : 
                      index % 3 === 0 ? 'bg-gradient-to-r from-purple-500 to-indigo-600' : 
                      index % 3 === 1 ? 'bg-gradient-to-r from-pink-500 to-rose-500' : 
                      'bg-gradient-to-r from-teal-400 to-emerald-500'} 
                    text-white font-bold mr-4 flex-shrink-0 shadow-md transform transition-transform hover:scale-110`}>
                    {isCompleted ? (
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                    ) : (
                      index + 1
                    )}
                  </div>
                  <div className={`${isCompleted ? 'bg-green-50 border-green-200' : 'bg-gray-50 border-gray-100'} hover:bg-white rounded-xl p-5 w-full border shadow-sm transition-all duration-300 hover:shadow-md`}>
                    <div className="flex justify-between items-start mb-4">
                      <div className="flex-1">
                        <h3 className={`font-semibold text-lg ${isCompleted ? 'text-green-800' : 'text-gray-800'}`}>
                          {step}
                          {isCompleted && (
                            <span className="ml-2 inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800">
                              <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                              </svg>
                              Completed
                            </span>
                          )}
                        </h3>
                      </div>
                      <div className="flex items-center space-x-2 ml-4">
                        {isCompleted ? (
                          <button
                            onClick={() => handleUnmarkSubskillComplete(step)}
                            className="inline-flex items-center px-3 py-1 border border-orange-300 text-orange-700 bg-orange-50 rounded-full text-sm font-medium hover:bg-orange-100 transition-colors duration-200"
                          >
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6" />
                            </svg>
                            Unmark
                          </button>
                        ) : (
                          <button
                            onClick={() => handleMarkSubskillComplete(step)}
                            className="inline-flex items-center px-3 py-1 border border-green-300 text-green-700 bg-green-50 rounded-full text-sm font-medium hover:bg-green-100 transition-colors duration-200"
                          >
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                            </svg>
                            Mark Complete
                          </button>
                        )}
                        <button
                          onClick={() => handleStartQuiz(skillName, step)}
                          className="inline-flex items-center px-3 py-1 border border-indigo-300 text-indigo-700 bg-indigo-50 rounded-full text-sm font-medium hover:bg-indigo-100 transition-colors duration-200"
                        >
                          <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                          </svg>
                          Quiz
                        </button>
                      </div>
                    </div>
                    
                    {/* Resources for this skill */}
                    <div className="w-full">
                      <h4 className="text-sm font-medium text-gray-700 mb-2 flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-2 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                        </svg>
                        Recommended Resources:
                      </h4>
                      {loadingResources[step] ? (
                        <div className="flex justify-center py-4">
                          <LoadingSpinner size="small" />
                          <span className="ml-2 text-gray-600">Loading high-quality resources...</span>
                        </div>
                      ) : resources[step] && resources[step].length > 0 ? (
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                          {resources[step].map((resource, resourceIndex) => (
                            <ResourceCard 
                              key={resource.id || `${step}_${resourceIndex}`} 
                              resource={resource} 
                            />
                          ))}
                        </div>
                      ) : resources[step] !== undefined && resources[step].length === 0 ? (
                        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 text-center">
                          <div className="flex items-center justify-center mb-2">
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-blue-600 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <p className="text-blue-800 font-medium">Ready to Learn</p>
                          </div>
                          <p className="text-blue-700 text-sm">
                            Start exploring <strong>{step}</strong> with hands-on practice and projects.
                          </p>
                          <p className="text-blue-600 text-xs mt-1">
                            Take the quiz when you're ready to test your knowledge!
                          </p>
                        </div>
                      ) : (
                        <div className="bg-gray-50 border border-gray-200 rounded-lg p-4 text-center">
                          <div className="flex items-center justify-center mb-2">
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-gray-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                            </svg>
                            <p className="text-gray-700 font-medium">Preparing Resources</p>
                          </div>
                          <p className="text-gray-600 text-sm">
                            Setting up learning materials for <strong>{step}</strong>.
                          </p>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Skill Tree Visualization */}
        {skillTree && (
          <div className="bg-white rounded-2xl shadow-lg p-8 mb-8 transition-all duration-300 hover:shadow-xl">
            <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-indigo-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z" />
              </svg>
              Skill Breakdown
            </h2>
            
            <div className="border-l-2 border-indigo-200 pl-6 ml-4">
              <div className="mb-6 p-4 bg-gradient-to-r from-indigo-50 to-purple-50 rounded-lg">
                <h3 className="font-bold text-xl text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600 mb-2">{skillTree.name}</h3>
                {skillTree.description && (
                  <p className="text-gray-600">{skillTree.description}</p>
                )}
              </div>
              <div className="ml-6 space-y-6">
                {skillTree.children.map((child, index) => (
                  <div key={index} className="border-l-2 border-pink-200 pl-4 py-2">
                    <div className="flex justify-between items-start mb-2">
                      <h4 className="font-semibold text-lg text-pink-700">{child.name}</h4>
                      <button
                        onClick={() => handleStartQuiz(skillTree.name, child.name)}
                        className="bg-gradient-to-r from-green-500 to-teal-600 hover:from-green-600 hover:to-teal-700 text-white px-4 py-2 rounded-full text-sm font-medium transition-all duration-300 transform hover:scale-105 shadow-md flex items-center"
                      >
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                        </svg>
                        Take Quiz
                      </button>
                    </div>
                    {child.children && child.children.length > 0 && (
                      <div className="ml-4 mt-3 space-y-3 bg-gray-50 p-3 rounded-lg">
                        {child.children.map((grandchild, idx) => (
                          <div key={idx} className="flex items-center justify-between">
                            <div className="flex items-center text-gray-700">
                              <span className="w-2 h-2 bg-indigo-400 rounded-full mr-2"></span>
                              {grandchild.name}
                            </div>
                            <button
                              onClick={() => handleStartQuiz(child.name, grandchild.name)}
                              className="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-xs font-medium transition-all duration-200 flex items-center"
                            >
                              <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                              </svg>
                              Quiz
                            </button>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Quiz Modal */}
      {showQuiz && (
        <QuizComponent
          skillName={currentQuizSkill.skillName}
          subskillName={currentQuizSkill.subskillName}
          onComplete={handleQuizComplete}
          onClose={handleCloseQuiz}
        />
      )}
    </div>
  );
};

export default LearningPath;
