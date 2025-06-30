import React, { useState } from 'react';
import ProgressBar from './ProgressBar';
import { Link } from 'react-router-dom';

const LearningPathCard = ({
  skill,
  subskills = [],
  completedSubskills = new Set(),
  onMarkComplete,
  onUnmarkComplete,
  onQuiz,
  onRemove,
  progress = 0,
  showRemove = false,
  step,
  index,
  currentStep,
  setCurrentStep,
  getResourceIcon
}) => {
  const [showQuiz, setShowQuiz] = useState(false);
  const [quizAnswers, setQuizAnswers] = useState({});
  const [quizSubmitted, setQuizSubmitted] = useState(false);
  const [quizScore, setQuizScore] = useState(0);

  const handleQuizAnswer = (questionIndex, answerIndex) => {
    setQuizAnswers(prev => ({
      ...prev,
      [questionIndex]: answerIndex
    }));
  };

  const submitQuiz = () => {
    let score = 0;
    step.quiz.questions.forEach((question, index) => {
      if (quizAnswers[index] === question.correct) {
        score++;
      }
    });
    setQuizScore(score);
    setQuizSubmitted(true);
    
    // If passed (>= 70%), mark as completed
    if (score / step.quiz.questions.length >= 0.7) {
      // Mark step as completed
      setTimeout(() => {
        setShowQuiz(false);
        setCurrentStep(currentStep + 1);
      }, 2000);
    }
  };

  const resetQuiz = () => {
    setQuizAnswers({});
    setQuizSubmitted(false);
    setQuizScore(0);
  };

  return (
    <div className={`bg-white rounded-2xl shadow-lg border-2 transition-all duration-300 ${
      index === currentStep ? 'border-indigo-300 shadow-xl' : 'border-gray-100'
    }`}>
      <div className="p-8">
        {/* Step Header */}
        <div className="flex items-start justify-between mb-6">
          <div className="flex items-start space-x-4">
            <div className={`w-12 h-12 rounded-full flex items-center justify-center font-bold text-lg ${
              step.completed 
                ? 'bg-green-100 text-green-600' 
                : index === currentStep 
                  ? 'bg-indigo-100 text-indigo-600' 
                  : 'bg-gray-100 text-gray-500'
            }`}>
              {step.completed ? '✓' : index + 1}
            </div>
            <div className="flex-1">
              <h3 className="text-2xl font-bold text-gray-900 mb-2">{step.title}</h3>
              <p className="text-gray-600 mb-4">{step.description}</p>
              <div className="flex items-center text-sm text-gray-500">
                <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                {step.duration}
              </div>
            </div>
          </div>
          
          {index === currentStep && (
            <div className="flex space-x-2">
              <button
                onClick={() => setShowQuiz(!showQuiz)}
                className="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-4 py-2 rounded-lg font-medium hover:from-purple-600 hover:to-pink-600 transition-all duration-300"
              >
                {showQuiz ? 'Hide Quiz' : 'Take Quiz'}
              </button>
            </div>
          )}
        </div>

        {/* Resources */}
        <div className="mb-6">
          <h4 className="font-semibold text-gray-900 mb-4">Learning Resources</h4>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {step.resources.map((resource, resIndex) => (
              <div key={resIndex} className="border border-gray-200 rounded-xl p-4 hover:shadow-md transition-shadow duration-300">
                <div className="flex items-start space-x-3">
                  <span className="text-2xl">{getResourceIcon(resource.type)}</span>
                  <div className="flex-1">
                    <h5 className="font-medium text-gray-900 mb-1">{resource.title}</h5>
                    <p className="text-sm text-gray-600 mb-2">{resource.provider}</p>
                    <p className="text-xs text-gray-500">{resource.duration}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Quiz Section */}
        {showQuiz && (
          <div className="border-t border-gray-200 pt-6">
            <h4 className="font-semibold text-gray-900 mb-4">📝 Knowledge Check</h4>
            
            {!quizSubmitted ? (
              <div className="space-y-6">
                {step.quiz.questions.map((question, qIndex) => (
                  <div key={qIndex} className="bg-gray-50 rounded-xl p-6">
                    <h5 className="font-medium text-gray-900 mb-4">
                      {qIndex + 1}. {question.question}
                    </h5>
                    <div className="space-y-2">
                      {question.options.map((option, oIndex) => (
                        <label key={oIndex} className="flex items-center cursor-pointer">
                          <input
                            type="radio"
                            name={`question-${qIndex}`}
                            value={oIndex}
                            onChange={() => handleQuizAnswer(qIndex, oIndex)}
                            className="mr-3 text-indigo-600 focus:ring-indigo-500"
                          />
                          <span className="text-gray-700">{option}</span>
                        </label>
                      ))}
                    </div>
                  </div>
                ))}
                
                <div className="flex justify-end space-x-4">
                  <button
                    onClick={() => setShowQuiz(false)}
                    className="border border-gray-300 text-gray-700 px-6 py-2 rounded-lg hover:bg-gray-50 transition-colors duration-300"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={submitQuiz}
                    disabled={Object.keys(quizAnswers).length !== step.quiz.questions.length}
                    className="bg-gradient-to-r from-indigo-600 to-blue-600 text-white px-6 py-2 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed hover:from-indigo-700 hover:to-blue-700 transition-all duration-300"
                  >
                    Submit Quiz
                  </button>
                </div>
              </div>
            ) : (
              <div className="text-center py-8">
                <div className={`w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 ${
                  quizScore / step.quiz.questions.length >= 0.7 
                    ? 'bg-green-100 text-green-600' 
                    : 'bg-red-100 text-red-600'
                }`}>
                  {quizScore / step.quiz.questions.length >= 0.7 ? '🎉' : '😔'}
                </div>
                
                <h5 className="text-xl font-bold text-gray-900 mb-2">
                  Quiz Completed!
                </h5>
                <p className="text-gray-600 mb-4">
                  You scored {quizScore} out of {step.quiz.questions.length} questions
                </p>
                
                {quizScore / step.quiz.questions.length >= 0.7 ? (
                  <div className="bg-green-50 border border-green-200 rounded-xl p-4 mb-4">
                    <p className="text-green-800 font-medium">
                      🎊 Congratulations! You passed this module. Moving to the next step...
                    </p>
                  </div>
                ) : (
                  <div className="bg-red-50 border border-red-200 rounded-xl p-4 mb-4">
                    <p className="text-red-800 font-medium">
                      You need at least 70% to pass. Review the materials and try again.
                    </p>
                    <button
                      onClick={resetQuiz}
                      className="mt-3 bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition-colors duration-300"
                    >
                      Retake Quiz
                    </button>
                  </div>
                )}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default LearningPathCard;
