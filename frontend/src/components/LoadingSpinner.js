import React from 'react';

const LoadingSpinner = ({ 
  size = 'default', // small, default, large
  color = 'primary', // primary, secondary, success, accent
  type = 'default', // default, orbit, pulse, dots, bars
  text = 'Loading...',
  showText = true,
}) => {
  // Size classes
  const getSizeClasses = () => {
    switch (size) {
      case 'small':
        return { spinner: 'h-10 w-10', text: 'text-sm', dot: 'h-2 w-2' };
      case 'large':
        return { spinner: 'h-24 w-24', text: 'text-lg', dot: 'h-6 w-6' };
      default:
        return { spinner: 'h-16 w-16', text: 'text-base', dot: 'h-4 w-4' };
    }
  };
  
  // Color classes
  const getColorClasses = () => {
    switch (color) {
      case 'secondary':
        return { border: 'border-purple-600', gradient: 'from-purple-500 to-pink-600', text: 'text-purple-600' };
      case 'success':
        return { border: 'border-emerald-600', gradient: 'from-emerald-500 to-green-600', text: 'text-emerald-600' };
      case 'accent':
        return { border: 'border-amber-600', gradient: 'from-amber-500 to-orange-600', text: 'text-amber-600' };
      default:
        return { border: 'border-indigo-600', gradient: 'from-indigo-500 to-blue-600', text: 'text-indigo-600' };
    }
  };
  
  const sizeClasses = getSizeClasses();
  const colorClasses = getColorClasses();
  
  // Render different spinner types
  const renderSpinner = () => {
    switch (type) {
      case 'orbit':
        return (
          <div className="relative">
            {/* Planet */}
            <div className={`${sizeClasses.spinner} rounded-full bg-gradient-to-r ${colorClasses.gradient} shadow-lg`}></div>
            
            {/* Orbiting elements */}
            <div className="absolute inset-0 animate-spin" style={{ animationDuration: '3s' }}>
              <div className={`absolute top-0 ${sizeClasses.dot} bg-white rounded-full shadow-lg transform -translate-x-1/2`}></div>
            </div>
            
            <div className="absolute inset-0 animate-spin" style={{ animationDuration: '5s', animationDirection: 'reverse' }}>
              <div className={`absolute bottom-0 ${sizeClasses.dot} bg-white rounded-full shadow-lg transform -translate-x-1/2`}></div>
            </div>
          </div>
        );
      
      case 'pulse':
        return (
          <div className="relative">
            <div className={`${sizeClasses.spinner} rounded-full bg-gradient-to-r ${colorClasses.gradient} animate-pulse-slow shadow-lg`}></div>
            <div className={`absolute inset-0 ${sizeClasses.spinner} rounded-full bg-gradient-to-r ${colorClasses.gradient} animate-pulse-slow opacity-60 shadow-lg`} style={{ animationDelay: '0.5s' }}></div>
            <div className={`absolute inset-0 ${sizeClasses.spinner} rounded-full bg-gradient-to-r ${colorClasses.gradient} animate-pulse-slow opacity-30 shadow-lg`} style={{ animationDelay: '1s' }}></div>
          </div>
        );
        
      case 'dots':
        return (
          <div className="flex space-x-2">
            {[...Array(4)].map((_, i) => (
              <div 
                key={i} 
                className={`rounded-full bg-gradient-to-r ${colorClasses.gradient} animate-bounce-slow ${sizeClasses.dot}`} 
                style={{ animationDelay: `${i * 0.15}s` }}
              ></div>
            ))}
          </div>
        );
        
      case 'bars':
        return (
          <div className="flex space-x-1 items-end">
            {[...Array(5)].map((_, i) => {
              const maxHeight = parseInt(sizeClasses.spinner.split('h-')[1], 10);
              const height = Math.max(4, Math.floor(maxHeight / 2) + (i % 3) * 4);
              
              return (
                <div 
                  key={i} 
                  className={`w-2 bg-gradient-to-t ${colorClasses.gradient} rounded-t-lg animate-pulse-slow`} 
                  style={{ 
                    height: `${height}px`, 
                    animationDelay: `${i * 0.15}s` 
                  }}
                ></div>
              );
            })}
          </div>
        );
        
      default:
        return (
          <div className="relative">
            {/* Inner spinner */}
            <div className={`animate-spin rounded-full ${sizeClasses.spinner} border-4 border-t-transparent ${colorClasses.border}`}></div>
            
            {/* Outer spinner (slower) */}
            <div className={`absolute top-0 left-0 animate-spin rounded-full ${sizeClasses.spinner} border-4 border-dashed border-t-transparent ${colorClasses.border} opacity-30`} style={{ animationDuration: '3s' }}></div>
            
            {/* Center dot */}
            <div className={`absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 ${sizeClasses.dot} bg-gradient-to-r ${colorClasses.gradient} rounded-full`}></div>
          </div>
        );
    }
  };
  
  return (
    <div className="flex flex-col justify-center items-center h-64">
      {renderSpinner()}
      
      {showText && (
        <p className={`mt-4 ${colorClasses.text} font-medium animate-pulse ${sizeClasses.text}`}>
          {text}
        </p>
      )}
    </div>
  );
};

export default LoadingSpinner;
