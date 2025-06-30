import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getSkill, getResourcesBySkillName, getSkillProgress, updateProgress } from '../api';
import ResourceCard from '../components/ResourceCard';
import ProgressBar from '../components/ProgressBar';
import LoadingSpinner from '../components/LoadingSpinner';
import PageTransition from '../components/PageTransition';
import { useToast } from '../contexts/ToastContext';

const SkillDetail = () => {  const { skillId } = useParams();
  const [skill, setSkill] = useState(null);
  const [resources, setResources] = useState([]);
  const [progress, setProgress] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const toast = useToast();
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        // First get the skill to get its name
        const skillResponse = await getSkill(skillId);
        setSkill(skillResponse.data);
        
        // Then use the skill name to get enhanced resources
        const skillName = skillResponse.data.name;
        const resourcesResponse = await getResourcesBySkillName(skillName);
        setResources(resourcesResponse.data[skillName] || []);
        
        // Get progress if available
        try {
          const progressResponse = await getSkillProgress(skillId);
          setProgress(progressResponse.data);
        } catch (err) {
          // No progress yet for this skill
          setProgress(null);
        }
      } catch (err) {
        console.error('Error fetching skill data:', err);
        setError('Failed to load skill data');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [skillId]);

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-[60vh]">
        <LoadingSpinner />
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-gradient-to-r from-red-50 to-red-100 border-l-4 border-red-500 text-red-700 p-6 rounded-xl shadow-md mb-6 flex items-start">
        <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 mr-3 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <div>
          <h3 className="font-bold text-lg mb-1">Error</h3>
          <p>{error}</p>
        </div>
      </div>
    );
  }
  if (!skill) {
    return (
      <div className="text-center p-8 bg-white rounded-2xl shadow-lg border border-gray-100 max-w-lg mx-auto mt-10">
        <svg xmlns="http://www.w3.org/2000/svg" className="h-20 w-20 text-gray-300 mx-auto mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h2 className="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-red-600 to-orange-600 mb-4">Skill not found</h2>
        <p className="text-gray-600 mb-6">We couldn't find the skill you're looking for. It may have been removed or doesn't exist.</p>
        <Link to="/dashboard" className="inline-flex items-center px-5 py-2 rounded-xl bg-gradient-to-r from-indigo-600 to-blue-600 text-white transition-all duration-300 transform hover:scale-105 shadow-md">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M9.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L7.414 9H15a1 1 0 110 2H7.414l2.293 2.293a1 1 0 010 1.414z" clipRule="evenodd" />
          </svg>
          Return to Dashboard
        </Link>
      </div>
    );
  }  return (
    <PageTransition>
      <div className="animate-fadeIn pt-16">
        {/* Skill Header */}
      <div className="mb-8 relative">
        <div className="flex items-center mb-3">
          <Link to="/dashboard" className="text-indigo-600 hover:text-indigo-800 flex items-center group">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1 transition-transform duration-300 group-hover:-translate-x-1" viewBox="0 0 20 20" fill="currentColor">
              <path fillRule="evenodd" d="M9.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L7.414 9H15a1 1 0 110 2H7.414l2.293 2.293a1 1 0 010 1.414z" clipRule="evenodd" />
            </svg>
            Dashboard
          </Link>
          <span className="text-gray-400 mx-2">›</span>
          <span className="text-gray-700 font-medium">{skill.name.toLowerCase()}</span>
        </div>
        
        {/* Make description the main title instead of skill name */}
        <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-blue-500 mb-6 mt-8">{skill.description || skill.name}</h1>
        
        <div className="absolute -top-6 -right-6 w-24 h-24 bg-gradient-to-br from-indigo-500 to-blue-500 rounded-full opacity-10"></div>
      </div>      {/* Progress Section */}
      <div className="bg-white rounded-2xl shadow-lg p-6 mb-8 border border-gray-100 hover:shadow-xl transition-all duration-300 transform relative overflow-hidden">
        <div className="absolute -top-12 -right-12 w-32 h-32 rounded-full bg-gradient-to-br from-indigo-500 to-blue-500 opacity-10"></div>
        <div className="absolute -bottom-12 -left-12 w-32 h-32 rounded-full bg-gradient-to-tr from-blue-500 to-indigo-500 opacity-10"></div>
        
        <h2 className="text-xl font-semibold text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-blue-600 mb-5 flex items-center">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-8.707l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 001.414 1.414L9 9.414V13a1 1 0 102 0V9.414l1.293 1.293a1 1 0 001.414-1.414z" clipRule="evenodd" />
          </svg>
          Your Progress
        </h2>
        
        <div className="mb-6 relative">
          <ProgressBar 
            percentage={progress ? progress.progress_percentage : 0}
            label={progress?.completed ? "Completed!" : "In Progress"}
          />
          
          {progress?.completed && (
            <div className="absolute -top-4 -right-2 transform rotate-12">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-green-500" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
            </div>
          )}
        </div>
      </div>      {/* Resources Section */}
      <div className="mb-8 relative">
        <div className="absolute -bottom-6 -left-6 w-24 h-24 bg-gradient-to-br from-teal-500 to-emerald-500 rounded-full opacity-10"></div>
        
        <h2 className="text-xl font-semibold text-transparent bg-clip-text bg-gradient-to-r from-teal-600 to-emerald-600 mb-4 flex items-center">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
            <path d="M7 3a1 1 0 000 2h6a1 1 0 100-2H7zM4 7a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1zM2 11a2 2 0 012-2h12a2 2 0 012 2v4a2 2 0 01-2 2H4a2 2 0 01-2-2v-4z" />
          </svg>
          Learning Resources
        </h2>
        
        {resources.length === 0 ? (
          <div className="bg-white rounded-2xl shadow-md p-8 text-center border border-gray-100">
            <div className="flex flex-col items-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-16 w-16 text-gray-300 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
              <p className="text-gray-600">No resources available for this skill yet.</p>
            </div>
          </div>
        ) : (
          <div className="space-y-4 relative">
            {resources.map(resource => (
              <ResourceCard key={resource.id} resource={resource} />
            ))}
          </div>
        )}
      </div>
      </div>
    </PageTransition>
  );
};

export default SkillDetail;
