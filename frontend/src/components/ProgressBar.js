import React, { useEffect, useState } from 'react';

const ProgressBar = ({ 
  percentage, 
  label, 
  color = 'default',
  showPercentage = true,
  height = 'default', // thin, default, thick
  animated = true,
  striped = false,
  rounded = true,
  className = ''
}) => {
  const [displayedPercentage, setDisplayedPercentage] = useState(0);
  
  // Animate the percentage on mount
  useEffect(() => {
    const roundedPercentage = Math.round(percentage);
    const step = roundedPercentage > 30 ? 2 : 1;
    
    if (displayedPercentage < roundedPercentage) {
      const timer = setTimeout(() => {
        setDisplayedPercentage(prev => Math.min(prev + step, roundedPercentage));
      }, 20);
      return () => clearTimeout(timer);
    }
  }, [displayedPercentage, percentage]);

  // Define gradient colors for different progress bars
  const getGradient = () => {
    switch(color) {
      case 'success':
        return 'from-emerald-500 to-green-500';
      case 'warning':
        return 'from-amber-500 to-yellow-500';
      case 'danger':
        return 'from-rose-500 to-red-500';
      case 'info':
        return 'from-sky-500 to-blue-500';
      case 'purple':
        return 'from-violet-500 to-purple-500';
      case 'cosmic':
        return 'from-indigo-500 via-purple-500 to-pink-500';
      case 'sunset':
        return 'from-red-500 via-orange-500 to-yellow-500';
      case 'ocean':
        return 'from-cyan-500 via-blue-500 to-indigo-500';
      default:
        return 'from-indigo-600 to-blue-500';
    }
  };
  
  // Get height class
  const getHeightClass = () => {
    switch(height) {
      case 'thin':
        return 'h-1.5';
      case 'thick':
        return 'h-4';
      default:
        return 'h-3';
    }
  };
  
  // Get rounded class
  const getRoundedClass = () => {
    return rounded ? 'rounded-full' : 'rounded-sm';
  };
    const gradient = getGradient();
  const heightClass = getHeightClass();
  const roundedClass = getRoundedClass();
  // Use the percentage directly instead of creating a redundant variable
  
  return (
    <div className={`w-full ${className}`}>
      {label && (
        <div className="flex justify-between items-center mb-1">
          <div className="text-sm font-medium text-gray-700">{label}</div>
          {showPercentage && (
            <div className="text-xs font-semibold bg-gray-100 text-gray-700 py-0.5 px-2 rounded-full">
              {displayedPercentage}%
            </div>
          )}
        </div>
      )}
      
      <div className={`w-full bg-gray-100 ${roundedClass} ${heightClass} shadow-inner overflow-hidden`}>
        <div
          className={`bg-gradient-to-r ${gradient} ${heightClass} ${roundedClass} transition-all duration-1000 ease-out relative 
            ${animated ? 'animate-gradientFlow' : ''} 
            ${striped ? 'bg-stripes' : ''}`}
          style={{ width: `${displayedPercentage}%` }}
        >
          {/* Animated shine effect */}
          <div className="absolute top-0 bottom-0 left-0 right-0 w-full h-full opacity-20 animate-shimmer"></div>
          
          {/* Progress dots for milestones */}
          {percentage >= 25 && (
            <div className="absolute top-1/2 left-1/4 transform -translate-y-1/2 -translate-x-1/2 w-2 h-2 bg-white rounded-full shadow-sm"></div>
          )}
          {percentage >= 50 && (
            <div className="absolute top-1/2 left-1/2 transform -translate-y-1/2 -translate-x-1/2 w-2 h-2 bg-white rounded-full shadow-sm"></div>
          )}
          {percentage >= 75 && (
            <div className="absolute top-1/2 left-3/4 transform -translate-y-1/2 -translate-x-1/2 w-2 h-2 bg-white rounded-full shadow-sm"></div>
          )}
        </div>
      </div>
      
      {!label && showPercentage && (
        <div className="text-xs text-gray-500 mt-1 text-right">{displayedPercentage}% Complete</div>
      )}
    </div>
  );
};

export default ProgressBar;
