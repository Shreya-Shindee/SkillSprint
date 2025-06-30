import React from 'react';
import { Link } from 'react-router-dom';
import ProgressBar from './ProgressBar';

const SkillCard = ({ skill, showTrash = false, onTrashClick }) => {
  // Function to determine gradient based on skill name (for variety)
  const getGradient = () => {
    const firstChar = skill.name.charAt(0).toLowerCase();
    if (firstChar <= 'g') return 'from-indigo-600 to-blue-500'; // A-G
    if (firstChar <= 'n') return 'from-purple-600 to-pink-500'; // H-N
    if (firstChar <= 't') return 'from-teal-500 to-emerald-500'; // O-T
    return 'from-orange-500 to-amber-500'; // U-Z
  };

  // Trash icon SVG
  const TrashIcon = (
    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6M1 7h22M8 7V5a2 2 0 012-2h4a2 2 0 012 2v2" />
    </svg>
  );

  return (
    <div className="relative">
      <Link to={`/skills/${skill.id}`} className="transform transition-all duration-300 hover:scale-105 block">
        <div className="bg-white rounded-2xl shadow-md p-6 hover:shadow-xl transition-all duration-300 border border-gray-100 relative overflow-hidden">
          {/* Decorative gradient orb in the background */}
          <div className={`absolute -top-10 -right-10 w-24 h-24 rounded-full bg-gradient-to-br ${getGradient()} opacity-10`}></div>
          
          {/* Card content */}
          <div className="relative z-10">
            <div className="flex justify-between items-start mb-3">
              <h3 className={`text-lg font-bold text-transparent bg-clip-text bg-gradient-to-r ${getGradient()}`}>
                {skill.name}
              </h3>
              <span className={`inline-flex items-center justify-center px-2 py-1 text-xs font-medium rounded-full 
                ${skill.parent_id 
                  ? 'bg-purple-100 text-purple-800' 
                  : 'bg-blue-100 text-blue-800'}`}>
                {skill.parent_id ? 'Subskill' : 'Main Skill'}
              </span>
            </div>
            
            <p className="text-gray-600 mt-2 text-sm line-clamp-2">
              {skill.description || 'No description available'}
            </p>
            
            {/* Progress bar and trash icon for in-progress skills */}
            {showTrash && typeof skill.progress === 'number' && (
              <div className="mt-4 flex items-center gap-2">
                <div className="flex-1">
                  <ProgressBar percentage={skill.progress} showPercentage={false} height="default" />
                </div>
                <span className="text-sm font-semibold text-indigo-700 ml-2">{Math.round(skill.progress)}%</span>
                <button
                  className="ml-2 bg-red-100 hover:bg-red-200 text-red-600 rounded-full p-2 shadow transition-colors duration-200"
                  title="Remove from Continue Learning"
                  onClick={e => {
                    e.preventDefault();
                    e.stopPropagation();
                    if (window.confirm(`Are you sure you want to remove '${skill.name}' from Continue Learning? This will remove your progress for this skill.`)) {
                      if (onTrashClick) onTrashClick(skill);
                    }
                  }}
                >
                  {TrashIcon}
                </button>
              </div>
            )}
            
            <div className="mt-4 pt-3 border-t border-gray-100 flex justify-end items-center">
              <span className="text-sm font-medium inline-flex items-center group">
                <span className={`text-transparent bg-clip-text bg-gradient-to-r ${getGradient()}`}>View Details</span>
                <svg xmlns="http://www.w3.org/2000/svg" className={`h-4 w-4 ml-1 transition-transform duration-300 group-hover:translate-x-1 ${getGradient().includes('indigo') ? 'text-indigo-600' : getGradient().includes('purple') ? 'text-purple-600' : getGradient().includes('teal') ? 'text-teal-600' : 'text-orange-600'}`} viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
              </span>
            </div>
          </div>
        </div>
      </Link>
    </div>
  );
};

export default SkillCard;
