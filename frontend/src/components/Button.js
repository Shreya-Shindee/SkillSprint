import React from 'react';

const Button = ({ 
  children, 
  onClick, 
  type = 'primary', // primary, secondary, outline, danger, success, accent, glass
  size = 'md', // sm, md, lg
  className = '',
  disabled = false,
  fullWidth = false,
  isLoading = false,
  leftIcon = null,
  rightIcon = null,
  animated = true,
  ...props 
}) => {
  // Define styles based on button type
  const getButtonStyles = () => {
    switch (type) {
      case 'primary':
        return 'bg-gradient-to-r from-indigo-600 to-blue-600 text-white hover:shadow-lg hover:shadow-indigo-500/20 hover:from-indigo-700 hover:to-blue-700';
      case 'secondary':
        return 'bg-gradient-to-r from-purple-600 to-pink-600 text-white hover:shadow-lg hover:shadow-purple-500/20 hover:from-purple-700 hover:to-pink-700';
      case 'outline':
        return 'bg-transparent border border-gray-300 text-gray-700 hover:bg-gray-50 hover:border-gray-400';
      case 'danger':
        return 'bg-gradient-to-r from-red-600 to-red-500 text-white hover:shadow-lg hover:shadow-red-500/20 hover:from-red-700 hover:to-red-600';
      case 'success':
        return 'bg-gradient-to-r from-emerald-600 to-green-500 text-white hover:shadow-lg hover:shadow-emerald-500/20 hover:from-emerald-700 hover:to-green-600';
      case 'accent':
        return 'bg-gradient-to-r from-amber-500 to-orange-500 text-white hover:shadow-lg hover:shadow-amber-500/20 hover:from-amber-600 hover:to-orange-600';
      case 'glass':
        return 'bg-white/20 backdrop-blur-md border border-white/30 text-white hover:bg-white/30 hover:shadow-lg';
      default:
        return 'bg-gradient-to-r from-indigo-600 to-blue-600 text-white hover:shadow-lg hover:from-indigo-700 hover:to-blue-700';
    }
  };

  // Define sizes
  const getSizeStyles = () => {
    switch (size) {
      case 'sm':
        return 'text-xs px-3 py-1.5 rounded-lg';
      case 'md':
        return 'text-sm px-4 py-2 rounded-xl';
      case 'lg':
        return 'text-base px-6 py-3 rounded-xl';
      default:
        return 'text-sm px-4 py-2 rounded-xl';
    }
  };

  // Animation classes
  const getAnimationClasses = () => {
    if (!animated) return '';
    
    return 'transform transition-all duration-300 hover:scale-105 active:scale-95';
  };

  return (
    <button
      onClick={onClick}
      disabled={disabled || isLoading}
      className={`
        ${getButtonStyles()} 
        ${getSizeStyles()} 
        ${fullWidth ? 'w-full' : ''} 
        ${disabled ? 'opacity-50 cursor-not-allowed' : getAnimationClasses()} 
        font-medium shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50
        relative overflow-hidden shine-effect
        ${className}
      `}
      {...props}
    >
      {isLoading ? (
        <div className="flex items-center justify-center">
          <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-current" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          Loading...
        </div>
      ) : (
        <div className="flex items-center justify-center">
          {leftIcon && <span className="mr-2 transform transition-transform group-hover:translate-x-[-2px]">{leftIcon}</span>}
          {children}
          {rightIcon && <span className="ml-2 transform transition-transform group-hover:translate-x-[2px]">{rightIcon}</span>}
        </div>
      )}
    </button>
  );
};

export default Button;
