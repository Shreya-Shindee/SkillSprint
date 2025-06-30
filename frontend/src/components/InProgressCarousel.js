import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import SkillCard from './SkillCard';

const InProgressCarousel = ({ skills, onSkillRemove }) => {
  const [activeIndex, setActiveIndex] = useState(0);
  const navigate = useNavigate();

  if (!skills || skills.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-12 px-4 text-center bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50 rounded-xl border border-indigo-100 shadow-sm">
        <div className="w-24 h-24 flex items-center justify-center bg-gradient-to-br from-indigo-100 to-purple-100 rounded-full mb-4 shadow-lg">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
        </div>
        <h3 className="text-xl font-semibold text-gray-800 mb-2">Ready to start learning?</h3>
        <p className="text-gray-600 mb-6 max-w-md">Begin your learning journey by creating a personalized learning path tailored to your goals!</p>
        <button 
          onClick={() => {
            const createPathElement = document.getElementById('create-path');
            if (createPathElement) {
              createPathElement.scrollIntoView({ 
                behavior: 'smooth',
                block: 'center'
              });
              // Focus on the input field after scrolling
              setTimeout(() => {
                const inputField = createPathElement.querySelector('input[type="text"]');
                if (inputField) {
                  inputField.focus();
                }
              }, 500);
            }
          }}
          title="Scroll down to type a skill name and click Create to start your learning path"
          className="group inline-flex items-center px-6 py-3 bg-gradient-to-r from-indigo-600 to-purple-600 text-white font-medium rounded-xl hover:from-indigo-700 hover:to-purple-700 transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1 relative"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clipRule="evenodd" />
          </svg>
          Create your first learning path
          
          {/* Tooltip on hover */}
          <div className="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 px-3 py-2 bg-gray-900 text-white text-sm rounded-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300 whitespace-nowrap z-10">
            Type a skill name below and click Create!
            <div className="absolute top-full left-1/2 transform -translate-x-1/2 w-0 h-0 border-l-4 border-r-4 border-t-4 border-transparent border-t-gray-900"></div>
          </div>
        </button>
      </div>
    );
  }

  const displayedSkills = skills.filter(skill => !skill.parent_id).slice(0, 4);

  return (
    <div className="space-y-6">
      {/* Grid layout for better visual organization */}
      <div className="grid grid-cols-1 gap-6">
        {displayedSkills.map((skill, index) => (
          <div
            key={skill.id}
            className={`transform transition-all duration-300 hover:scale-105 ${
              activeIndex === index ? 'ring-2 ring-indigo-300 shadow-lg' : ''
            }`}
            onMouseEnter={() => setActiveIndex(index)}
          >
            <div className="relative group">
              <SkillCard
                skill={skill}
                showTrash={true}
                onTrashClick={() => {
                  if (window.confirm(`Are you sure you want to remove '${skill.name}' from Continue Learning? This will remove your progress for this skill.`)) {
                    onSkillRemove(skill.id);
                  }
                }}
                enhanced={true}
              />
              
              {/* Progress overlay with animation */}
              <div className="absolute top-4 right-4 bg-white/90 backdrop-blur-sm rounded-lg px-3 py-1 shadow-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                <div className="flex items-center space-x-2">
                  <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                  <span className="text-sm font-medium text-gray-700">
                    {skill.progress || 0}% Complete
                  </span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* View more button with enhanced styling */}
      {skills.filter(skill => !skill.parent_id).length > 4 && (
        <div className="flex justify-center mt-8">
          <button 
            onClick={() => navigate('/profile')}
            className="group inline-flex items-center px-6 py-3 border-2 border-indigo-200 text-indigo-700 bg-white rounded-xl hover:bg-indigo-50 hover:border-indigo-300 transition-all duration-300 shadow-sm hover:shadow-md"
          >
            <span className="font-medium">
              View all {skills.filter(skill => !skill.parent_id).length} in-progress skills
            </span>
            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-2 group-hover:translate-x-1 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </button>
        </div>
      )}

      {/* Quick stats */}
      {displayedSkills.length > 0 && (
        <div className="grid grid-cols-3 gap-4 mt-6 p-4 bg-gradient-to-r from-indigo-50 to-purple-50 rounded-xl border border-indigo-100">
          <div className="text-center">
            <div className="text-2xl font-bold text-indigo-600">
              {displayedSkills.length}
            </div>
            <div className="text-sm text-gray-600">Active Skills</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-purple-600">
              {Math.round(displayedSkills.reduce((acc, skill) => acc + (skill.progress || 0), 0) / displayedSkills.length)}%
            </div>
            <div className="text-sm text-gray-600">Avg Progress</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-green-600">
              {displayedSkills.filter(skill => (skill.progress || 0) > 80).length}
            </div>
            <div className="text-sm text-gray-600">Near Complete</div>
          </div>
        </div>
      )}
    </div>
  );
};

export default InProgressCarousel;
