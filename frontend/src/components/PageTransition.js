import React, { useEffect, useState } from 'react';

// PageTransition wraps page content to provide smooth transition animations
const PageTransition = ({ 
  children, 
  type = 'fade', // fade, slide, scale, bounce, reveal
  direction = 'up', // up, down, left, right (for slide transitions)
  duration = 'default', // fast, default, slow
  delay = 0 // in milliseconds
}) => {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    // Small delay to ensure transition happens after render
    const timer = setTimeout(() => {
      setIsVisible(true);
    }, 50 + delay);

    return () => clearTimeout(timer);
  }, [delay]);
  
  // Get duration class
  const getDurationClass = () => {
    switch (duration) {
      case 'fast':
        return 'duration-300';
      case 'slow':
        return 'duration-1000';
      default:
        return 'duration-500';
    }
  };
  
  // Get initial and final state classes based on transition type
  const getTransitionClasses = () => {
    // Base classes that apply to all transitions
    const baseClasses = `transition-all ${getDurationClass()} ease-out`;
    
    // Visible state is always opacity-100
    let visibleState = 'opacity-100 ';
    let hiddenState = 'opacity-0 ';
    
    switch (type) {
      case 'slide':
        if (direction === 'up') {
          visibleState += 'translate-y-0';
          hiddenState += 'translate-y-16';
        } else if (direction === 'down') {
          visibleState += 'translate-y-0';
          hiddenState += '-translate-y-16';
        } else if (direction === 'left') {
          visibleState += 'translate-x-0';
          hiddenState += 'translate-x-16';
        } else { // right
          visibleState += 'translate-x-0';
          hiddenState += '-translate-x-16';
        }
        break;
        
      case 'scale':
        visibleState += 'scale-100';
        hiddenState += 'scale-95';
        break;
        
      case 'bounce':
        if (isVisible) {
          return `${baseClasses} opacity-100 animate-bounce`;
        } else {
          return `${baseClasses} opacity-0`;
        }
        
      case 'reveal':
        // For reveal, we'll use a special clip-path transition
        if (isVisible) {
          return `${baseClasses} opacity-100 clip-path-revealed`;
        } else {
          return `${baseClasses} opacity-0 clip-path-hidden`;
        }
        
      default: // fade
        visibleState += 'translate-y-0';
        hiddenState += 'translate-y-4';
        break;
    }
    
    return `${baseClasses} ${isVisible ? visibleState : hiddenState}`;
  };

  return (
    <div className={getTransitionClasses()}>
      {children}
    </div>
  );
};

// CSS for clip-path transitions should be added to animations.css:
// .clip-path-revealed { clip-path: inset(0 0 0 0); }
// .clip-path-hidden { clip-path: inset(0 100% 0 0); }

export default PageTransition;
