import React, { useState, useEffect } from 'react';

const XPBar = ({ currentXP, nextLevelXP, skillName = "Programming", coursesCompleted = 0, badges = [] }) => {
  const [displayXP, setDisplayXP] = useState(0);
  const [isAnimating, setIsAnimating] = useState(false);
  
  useEffect(() => {
    // Animate XP counting up
    if (displayXP < currentXP) {
      setIsAnimating(true);
      const step = Math.ceil((currentXP - displayXP) / 20);
      const timer = setTimeout(() => {
        setDisplayXP(prev => Math.min(prev + step, currentXP));
      }, 30);
      return () => clearTimeout(timer);
    } else {
      setIsAnimating(false);
    }
  }, [displayXP, currentXP]);

  const percentage = Math.min((currentXP / nextLevelXP) * 100, 100);
  const level = Math.floor(currentXP / 1000) + 1;

  // Calculate learning achievements (stars for every 5 levels completed)
  const achievementStars = Math.floor(level / 5);
  const currentLevelProgress = level % 5;

  // Learning level titles
  const getLevelTitle = (level) => {
    if (level <= 5) return "Beginner";
    if (level <= 10) return "Learner";
    if (level <= 20) return "Skilled";
    if (level <= 35) return "Expert";
    if (level <= 50) return "Master";
    return "Guru";
  };

  return (
    <div className="bg-gradient-to-r from-indigo-50 via-blue-50 to-purple-50 rounded-xl shadow-lg p-6 border border-indigo-100 relative overflow-hidden">
      {/* Learning-themed decorative elements */}
      <div className="absolute -top-10 -right-10 w-40 h-40 bg-gradient-to-br from-blue-400 to-indigo-300 rounded-full opacity-10 animate-pulse-slow"></div>
      <div className="absolute -bottom-10 -left-10 w-40 h-40 bg-gradient-to-tr from-green-400 to-blue-300 rounded-full opacity-10 animate-pulse-slow"></div>
      
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-4 relative z-10">
        <div className="flex items-center space-x-4">
          {/* Learning Level Badge */}
          <div className="relative group">
            <div className="absolute inset-0 rounded-full bg-gradient-to-r from-blue-600 to-indigo-600 blur-md opacity-30 group-hover:opacity-40 transition-opacity duration-300"></div>
            <div className="w-16 h-16 rounded-full bg-gradient-to-br from-blue-600 via-indigo-600 to-purple-600 flex items-center justify-center text-white font-bold text-lg shadow-lg relative z-10 border-2 border-white/30 group-hover:scale-105 transition-transform duration-300">
              <div className="text-center">
                <div className="text-xl">{level}</div>
                <div className="text-xs opacity-80">LVL</div>
              </div>
            </div>
          </div>
          
          <div>
            <div className="flex items-center space-x-2">
              <span className="text-xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 animate-gradientFlow">
                {getLevelTitle(level)}
              </span>
              <span className="text-sm text-gray-600">in {skillName}</span>
            </div>
            
            {/* Learning Achievement Stars */}
            <div className="flex mt-1 items-center space-x-2">
              <div className="flex items-center">
                {[...Array(achievementStars)].map((_, i) => (
                  <svg key={i} className="w-5 h-5 text-yellow-500 animate-pulse-slow" style={{ animationDelay: `${i * 0.2}s` }} fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                  </svg>
                ))}
              </div>
              
              {/* Progress to next achievement */}
              {currentLevelProgress > 0 && (
                <div className="flex items-center space-x-2">
                  <div className="flex space-x-1">
                    {[...Array(5)].map((_, i) => (
                      <div 
                        key={i} 
                        className={`w-2 h-2 rounded-full transition-colors duration-300 ${
                          i < currentLevelProgress ? 'bg-blue-400' : 'bg-gray-300'
                        }`}
                      />
                    ))}
                  </div>
                  <span className="text-xs text-gray-500">{currentLevelProgress}/5 to next ⭐</span>
                </div>
              )}
            </div>
            
            {/* Learning Stats */}
            <div className="flex items-center space-x-4 mt-1 text-xs text-gray-600">
              <span>📚 {coursesCompleted} courses completed</span>
              {badges.length > 0 && <span>🏆 {badges.length} badges earned</span>}
            </div>
          </div>
        </div>
        
        {/* Learning XP Display */}
        <div className="mt-3 md:mt-0">
          <span className="px-4 py-2 bg-white rounded-xl shadow-sm border border-indigo-100 flex items-center space-x-2 group hover:shadow-md transition-all duration-300">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-green-500 group-hover:text-green-600 transition-colors duration-300" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <div className="font-medium text-indigo-900">
              <span className="text-green-600 font-semibold">{displayXP}</span>
              <span> / </span>
              <span className="text-blue-600">{nextLevelXP}</span>
              <span className="text-xs ml-1 text-gray-500">Learning XP</span>
            </div>
          </span>
        </div>
      </div>
      
      {/* Learning Progress Bar */}
      <div className="relative w-full">
        <div className="absolute inset-0 flex items-center justify-center z-10 opacity-0 hover:opacity-100 transition-opacity duration-300">
          <span className="text-xs font-semibold text-white bg-gradient-to-r from-blue-600 to-indigo-600 px-3 py-1 rounded-md shadow-sm">
            {Math.round(percentage)}% Complete
          </span>
        </div>
        
        {/* Enhanced Learning Progress Bar */}
        <div className="w-full bg-white/70 backdrop-blur-sm rounded-full h-6 shadow-inner overflow-hidden border border-indigo-100/50">
          <div
            className="bg-gradient-to-r from-green-500 via-blue-500 to-indigo-600 h-6 rounded-full transition-all duration-700 ease-out relative animate-gradientFlow"
            style={{ width: `${percentage}%` }}
          >
            {/* Learning progress shine effect */}
            <div className="absolute top-0 left-0 right-0 bottom-0 w-full h-full animate-shimmer"></div>
            
            {/* Learning milestone markers */}
            <div className="absolute inset-0">
              {[25, 50, 75].map(milestone => (
                percentage >= milestone && (
                  <div 
                    key={milestone}
                    className="absolute top-1/2 transform -translate-y-1/2 w-3 h-3 bg-white rounded-full shadow-sm border-2 border-green-400 flex items-center justify-center"
                    style={{ left: `${milestone}%`, marginLeft: '-6px' }}
                  >
                    <div className="w-1 h-1 bg-green-500 rounded-full"></div>
                  </div>
                )
              ))}
            </div>
            
            {/* Learning XP gain animations */}
            {isAnimating && (
              <>
                <div className="absolute right-2 top-1 animate-float" style={{ animationDelay: '0.1s' }}>
                  <div className="text-white text-xs font-bold">📖 +XP</div>
                </div>
                <div className="absolute right-8 -top-1 animate-float" style={{ animationDelay: '0.3s' }}>
                  <div className="text-white text-xs font-bold">🎯 +XP</div>
                </div>
              </>
            )}
          </div>
        </div>
        
        {/* Learning progress markers */}
        <div className="flex justify-between mt-2 px-1">
          <div className="text-xs text-gray-500 flex flex-col items-center">
            <span>📚</span>
            <span>Start</span>
          </div>
          <div className="text-xs text-gray-500 flex flex-col items-center">
            <span>🎯</span>
            <span>25%</span>
          </div>
          <div className="text-xs text-gray-500 flex flex-col items-center">
            <span>💡</span>
            <span>50%</span>
          </div>
          <div className="text-xs text-gray-500 flex flex-col items-center">
            <span>🏆</span>
            <span>75%</span>
          </div>
          <div className="text-xs text-gray-500 flex flex-col items-center">
            <span>⭐</span>
            <span>Master</span>
          </div>
        </div>
      </div>
      
      {/* Learning Progress Summary */}
      <div className="mt-4 text-center">
        <p className="text-sm text-gray-600">
          <span className="text-blue-600 font-medium">{nextLevelXP - currentXP} XP</span> needed to reach 
          <span className="text-indigo-600 font-medium"> {getLevelTitle(level + 1)} Level {level + 1}</span>
        </p>
        <p className="text-xs text-gray-500 mt-1">
          Keep learning to unlock new achievements and skills! 🚀
        </p>
      </div>
    </div>
  );
};

export default XPBar;
