import React, { useState, useEffect, useRef } from 'react';

const AnimatedNumber = ({ value, duration = 1000, prefix = '', suffix = '', className = '' }) => {
  const [displayValue, setDisplayValue] = useState(0);
  const startTime = useRef(null);
  const currentValueRef = useRef(0);
  const targetValueRef = useRef(value);
  
  useEffect(() => {
    targetValueRef.current = value;
    startTime.current = Date.now();
    currentValueRef.current = displayValue;
    
    const animateValue = () => {
      const currentTime = Date.now();
      const elapsedTime = currentTime - startTime.current;
      
      if (elapsedTime < duration) {
        const progress = elapsedTime / duration;
        const easeProgress = easeOutQuad(progress);
        const newValue = currentValueRef.current + (targetValueRef.current - currentValueRef.current) * easeProgress;
        
        setDisplayValue(Math.round(newValue));
        requestAnimationFrame(animateValue);
      } else {
        setDisplayValue(targetValueRef.current);
      }
    };
    
    requestAnimationFrame(animateValue);
    
    return () => {
      // Nothing to clean up explicitly, but this helps if we later add any cleanup
    };
  }, [value, duration]);
  
  // Easing function for smoother animation
  const easeOutQuad = (t) => t * (2 - t);
  
  return (
    <span className={className}>
      {prefix}{displayValue}{suffix}
    </span>
  );
};

export default AnimatedNumber;
