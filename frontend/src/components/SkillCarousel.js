import React, { useState, useRef, useEffect } from 'react';
import SkillCard from './SkillCard';

const SkillCarousel = ({ skills, title, showViewAll = true }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [canScrollLeft, setCanScrollLeft] = useState(false);
  const [canScrollRight, setCanScrollRight] = useState(true);
  const carouselRef = useRef(null);

  const itemsPerView = {
    sm: 1,
    md: 2,
    lg: 3,
    xl: 4
  };

  const [currentItemsPerView, setCurrentItemsPerView] = useState(3);

  useEffect(() => {
    const handleResize = () => {
      const width = window.innerWidth;
      if (width < 640) {
        setCurrentItemsPerView(itemsPerView.sm);
      } else if (width < 768) {
        setCurrentItemsPerView(itemsPerView.md);
      } else if (width < 1024) {
        setCurrentItemsPerView(itemsPerView.lg);
      } else {
        setCurrentItemsPerView(itemsPerView.xl);
      }
    };

    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  useEffect(() => {
    const maxIndex = Math.max(0, skills.length - currentItemsPerView);
    setCanScrollLeft(currentIndex > 0);
    setCanScrollRight(currentIndex < maxIndex);
  }, [currentIndex, skills.length, currentItemsPerView]);

  const scrollLeft = () => {
    setCurrentIndex(prev => Math.max(0, prev - 1));
  };

  const scrollRight = () => {
    const maxIndex = Math.max(0, skills.length - currentItemsPerView);
    setCurrentIndex(prev => Math.min(maxIndex, prev + 1));
  };

  const goToSlide = (index) => {
    const maxIndex = Math.max(0, skills.length - currentItemsPerView);
    setCurrentIndex(Math.min(index, maxIndex));
  };

  if (!skills || skills.length === 0) {
    return (
      <div className="bg-white rounded-2xl shadow-lg p-8 border border-gray-100">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">{title}</h2>
        <div className="flex flex-col items-center justify-center py-12 px-4 text-center bg-gray-50 rounded-xl border border-gray-100">
          <div className="w-24 h-24 flex items-center justify-center bg-indigo-100 rounded-full mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
            </svg>
          </div>
          <h3 className="text-lg font-medium text-gray-700 mb-2">No skills available</h3>
          <p className="text-gray-500">Start by creating your first learning path!</p>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-2xl shadow-lg p-8 border border-gray-100">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold text-gray-800 flex items-center">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 mr-2 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
          </svg>
          {title}
        </h2>
        {showViewAll && (
          <button className="text-indigo-600 hover:text-indigo-800 font-medium text-sm flex items-center transition-colors duration-200">
            View All
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </button>
        )}
      </div>
      
      <div className="relative">
        {/* Navigation Arrows */}
        {skills.length > currentItemsPerView && (
          <>
            <button
              onClick={scrollLeft}
              disabled={!canScrollLeft}
              className={`absolute left-0 top-1/2 transform -translate-y-1/2 -translate-x-4 z-10 w-12 h-12 rounded-full bg-white shadow-lg border border-gray-200 flex items-center justify-center transition-all duration-300 ${
                canScrollLeft 
                  ? 'hover:bg-indigo-50 hover:border-indigo-300 text-gray-700 hover:text-indigo-600 cursor-pointer' 
                  : 'text-gray-300 cursor-not-allowed opacity-50'
              }`}
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
            </button>

            <button
              onClick={scrollRight}
              disabled={!canScrollRight}
              className={`absolute right-0 top-1/2 transform -translate-y-1/2 translate-x-4 z-10 w-12 h-12 rounded-full bg-white shadow-lg border border-gray-200 flex items-center justify-center transition-all duration-300 ${
                canScrollRight 
                  ? 'hover:bg-indigo-50 hover:border-indigo-300 text-gray-700 hover:text-indigo-600 cursor-pointer' 
                  : 'text-gray-300 cursor-not-allowed opacity-50'
              }`}
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </button>
          </>
        )}

        {/* Carousel Container */}
        <div className="overflow-hidden rounded-xl">
          <div 
            ref={carouselRef}
            className="flex transition-transform duration-500 ease-in-out"
            style={{
              transform: `translateX(-${currentIndex * (100 / currentItemsPerView)}%)`,
              width: `${(skills.length / currentItemsPerView) * 100}%`
            }}
          >
            {skills.map((skill, index) => (
              <div
                key={skill.id || index}
                className="flex-shrink-0 px-3"
                style={{ width: `${100 / skills.length}%` }}
              >
                <div className="h-full">
                  <SkillCard skill={skill} />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Dots Indicator */}
        {skills.length > currentItemsPerView && (
          <div className="flex justify-center mt-6 space-x-2">
            {Array.from({ length: Math.ceil(skills.length / currentItemsPerView) }).map((_, index) => (
              <button
                key={index}
                onClick={() => goToSlide(index)}
                className={`w-2 h-2 rounded-full transition-all duration-300 ${
                  Math.floor(currentIndex / currentItemsPerView) === index
                    ? 'bg-indigo-600 w-8'
                    : 'bg-gray-300 hover:bg-gray-400'
                }`}
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default SkillCarousel;
