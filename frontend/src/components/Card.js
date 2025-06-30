import React from 'react';

const Card = ({ 
  children, 
  title, 
  subtitle, 
  icon,
  gradient = 'indigo',  // indigo, purple, teal, amber, cosmic, sunset, ocean
  hoverEffect = true,
  glassEffect = false,
  animation = '',  // '', 'fade', 'scale', 'float'
  className = '', 
  headerClassName = '',
  bodyClassName = '',
  ...props 
}) => {
  // Define gradient styles
  const getGradientStyles = () => {
    switch (gradient) {
      case 'indigo':
        return {
          orb: 'from-indigo-500 to-blue-500',
          title: 'from-indigo-600 to-blue-600',
          shadow: 'shadow-indigo-500/10'
        };
      case 'purple':
        return {
          orb: 'from-purple-500 to-pink-500',
          title: 'from-purple-600 to-pink-600',
          shadow: 'shadow-purple-500/10'
        };
      case 'teal':
        return {
          orb: 'from-teal-500 to-emerald-500',
          title: 'from-teal-600 to-emerald-600',
          shadow: 'shadow-teal-500/10'
        };
      case 'amber':
        return {
          orb: 'from-amber-500 to-orange-500',
          title: 'from-amber-600 to-orange-600',
          shadow: 'shadow-amber-500/10'
        };
      case 'cosmic':
        return {
          orb: 'from-violet-500 to-indigo-500',
          title: 'from-violet-600 to-indigo-600',
          shadow: 'shadow-violet-500/10'
        };
      case 'sunset':
        return {
          orb: 'from-red-500 to-orange-500',
          title: 'from-red-600 to-orange-600',
          shadow: 'shadow-red-500/10'
        };
      case 'ocean':
        return {
          orb: 'from-cyan-500 to-blue-500',
          title: 'from-cyan-600 to-blue-600',
          shadow: 'shadow-cyan-500/10'
        };
      default:
        return {
          orb: 'from-indigo-500 to-blue-500',
          title: 'from-indigo-600 to-blue-600',
          shadow: 'shadow-indigo-500/10'
        };
    }
  };

  // Animation styles
  const getAnimationStyles = () => {
    switch (animation) {
      case 'fade':
        return 'animate-fadeIn';
      case 'scale':
        return 'animate-scaleIn';
      case 'float':
        return 'animate-float';
      default:
        return '';
    }
  };

  // Hover effects
  const getHoverEffects = () => {
    if (!hoverEffect) return '';
    return 'hover:shadow-xl transition-all duration-300 transform hover:scale-102 hover:translate-y-[-4px]';
  };

  // Glass effect
  const getCardBaseStyles = () => {
    if (glassEffect) {
      return 'glass-card';
    }
    return `bg-white rounded-2xl shadow-md p-6 border border-gray-100 ${getGradientStyles().shadow}`;
  };

  const gradientStyles = getGradientStyles();

  return (
    <div 
      className={`
        ${getCardBaseStyles()}
        ${getHoverEffects()}
        ${getAnimationStyles()}
        relative overflow-hidden ${className}
      `}
      {...props}
    >
      {/* Decorative gradient orbs */}
      <div className={`absolute -top-12 -right-12 w-32 h-32 rounded-full bg-gradient-to-br animate-rotating ${gradientStyles.orb} opacity-10`}></div>
      <div className={`absolute -bottom-12 -left-12 w-32 h-32 rounded-full bg-gradient-to-tr animate-rotating ${gradientStyles.orb} opacity-10`}></div>
      
      {/* Card content */}
      <div className="relative z-10">
        {(title || subtitle) && (
          <div className={`mb-4 ${headerClassName}`}>
            {title && (
              <h3 className={`text-xl font-semibold text-transparent bg-clip-text bg-gradient-to-r animate-gradientFlow ${gradientStyles.title} flex items-center`}>
                {icon && <span className="mr-2 text-2xl">{icon}</span>}
                {title}
              </h3>
            )}
            {subtitle && <p className="text-gray-600 mt-1">{subtitle}</p>}
          </div>
        )}
        <div className={bodyClassName}>
          {children}
        </div>
      </div>
      
      {/* Shine effect overlay */}
      <div className="absolute inset-0 pointer-events-none opacity-0 hover:opacity-100 transition-opacity duration-700">
        <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent translate-x-[-100%] animate-shimmer"></div>
      </div>
    </div>
  );
};

export default Card;
