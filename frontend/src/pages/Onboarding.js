import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Onboarding = () => {
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState({
    name: '',
    experience: '',
    interests: [],
    goals: '',
    timeCommitment: ''
  });
  const navigate = useNavigate();

  const experiences = [
    { id: 'beginner', label: 'Complete Beginner', desc: 'New to learning online' },
    { id: 'some', label: 'Some Experience', desc: 'Taken a few online courses' },
    { id: 'experienced', label: 'Experienced', desc: 'Regular online learner' }
  ];

  const interests = [
    '💻 Programming', '🎨 Design', '📊 Data Science', '🚀 Entrepreneurship',
    '📱 Mobile Development', '🔒 Cybersecurity', '📈 Marketing', '🎯 Project Management',
    '🤖 AI & Machine Learning', '☁️ Cloud Computing', '📝 Writing', '🎵 Music'
  ];

  const timeCommitments = [
    '15-30 minutes/day', '30-60 minutes/day', '1-2 hours/day', '2+ hours/day'
  ];

  const handleInterestToggle = (interest) => {
    setFormData(prev => ({
      ...prev,
      interests: prev.interests.includes(interest)
        ? prev.interests.filter(i => i !== interest)
        : [...prev.interests, interest]
    }));
  };

  const handleComplete = () => {
    // Save onboarding data and redirect to dashboard
    localStorage.setItem('onboardingComplete', 'true');
    localStorage.setItem('userPreferences', JSON.stringify(formData));
    console.log('Onboarding completed, redirecting to dashboard');
    
    // Use navigate with replace to avoid back button issues
    navigate('/dashboard', { replace: true });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 to-blue-50 flex items-center justify-center p-4">
      <div className="bg-white rounded-3xl shadow-2xl p-8 max-w-2xl w-full">
        {/* Progress Bar */}
        <div className="mb-8">
          <div className="flex justify-between text-sm text-gray-500 mb-2">
            <span>Step {step} of 4</span>
            <span>{Math.round((step / 4) * 100)}% Complete</span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div 
              className="bg-gradient-to-r from-indigo-600 to-blue-600 h-2 rounded-full transition-all duration-500"
              style={{ width: `${(step / 4) * 100}%` }}
            ></div>
          </div>
        </div>

        {/* Step 1: Welcome & Name */}
        {step === 1 && (
          <div className="text-center">
            <h1 className="text-4xl font-bold text-gray-900 mb-4">
              Welcome to SkillSprint! 🎉
            </h1>
            <p className="text-gray-600 mb-8">
              Let's personalize your learning experience. What should we call you?
            </p>
            <input
              type="text"
              placeholder="Enter your name"
              value={formData.name}
              onChange={(e) => setFormData(prev => ({ ...prev, name: e.target.value }))}
              className="w-full px-6 py-4 text-lg border-2 border-gray-200 rounded-xl focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 outline-none transition-all duration-300 mb-8"
            />
            <button
              onClick={() => setStep(2)}
              disabled={!formData.name.trim()}
              className="bg-gradient-to-r from-indigo-600 to-blue-600 text-white px-8 py-4 rounded-xl font-semibold text-lg disabled:opacity-50 disabled:cursor-not-allowed hover:from-indigo-700 hover:to-blue-700 transition-all duration-300"
            >
              Continue
            </button>
          </div>
        )}

        {/* Step 2: Experience Level */}
        {step === 2 && (
          <div>
            <h2 className="text-3xl font-bold text-gray-900 mb-4">
              What's your learning experience?
            </h2>
            <p className="text-gray-600 mb-8">
              This helps us recommend the right difficulty level for you.
            </p>
            <div className="space-y-4 mb-8">
              {experiences.map((exp) => (
                <div
                  key={exp.id}
                  onClick={() => setFormData(prev => ({ ...prev, experience: exp.id }))}
                  className={`p-6 border-2 rounded-xl cursor-pointer transition-all duration-300 ${
                    formData.experience === exp.id
                      ? 'border-indigo-500 bg-indigo-50'
                      : 'border-gray-200 hover:border-indigo-300'
                  }`}
                >
                  <h3 className="font-semibold text-lg text-gray-900">{exp.label}</h3>
                  <p className="text-gray-600">{exp.desc}</p>
                </div>
              ))}
            </div>
            <div className="flex gap-4">
              <button
                onClick={() => setStep(1)}
                className="flex-1 border-2 border-gray-300 text-gray-700 px-6 py-3 rounded-xl font-semibold hover:bg-gray-50 transition-colors duration-300"
              >
                Back
              </button>
              <button
                onClick={() => setStep(3)}
                disabled={!formData.experience}
                className="flex-1 bg-gradient-to-r from-indigo-600 to-blue-600 text-white px-6 py-3 rounded-xl font-semibold disabled:opacity-50 disabled:cursor-not-allowed hover:from-indigo-700 hover:to-blue-700 transition-all duration-300"
              >
                Continue
              </button>
            </div>
          </div>
        )}

        {/* Step 3: Interests */}
        {step === 3 && (
          <div>
            <h2 className="text-3xl font-bold text-gray-900 mb-4">
              What interests you?
            </h2>
            <p className="text-gray-600 mb-8">
              Select all that apply. We'll suggest relevant learning paths.
            </p>
            <div className="grid grid-cols-2 gap-3 mb-8">
              {interests.map((interest) => (
                <div
                  key={interest}
                  onClick={() => handleInterestToggle(interest)}
                  className={`p-4 border-2 rounded-xl cursor-pointer text-center transition-all duration-300 ${
                    formData.interests.includes(interest)
                      ? 'border-indigo-500 bg-indigo-50 text-indigo-700'
                      : 'border-gray-200 hover:border-indigo-300'
                  }`}
                >
                  {interest}
                </div>
              ))}
            </div>
            <div className="flex gap-4">
              <button
                onClick={() => setStep(2)}
                className="flex-1 border-2 border-gray-300 text-gray-700 px-6 py-3 rounded-xl font-semibold hover:bg-gray-50 transition-colors duration-300"
              >
                Back
              </button>
              <button
                onClick={() => setStep(4)}
                disabled={formData.interests.length === 0}
                className="flex-1 bg-gradient-to-r from-indigo-600 to-blue-600 text-white px-6 py-3 rounded-xl font-semibold disabled:opacity-50 disabled:cursor-not-allowed hover:from-indigo-700 hover:to-blue-700 transition-all duration-300"
              >
                Continue
              </button>
            </div>
          </div>
        )}

        {/* Step 4: Goals & Time Commitment */}
        {step === 4 && (
          <div>
            <h2 className="text-3xl font-bold text-gray-900 mb-4">
              Almost done! 🎯
            </h2>
            <p className="text-gray-600 mb-6">
              Tell us about your goals and how much time you can dedicate.
            </p>
            
            <div className="mb-6">
              <label className="block text-lg font-semibold text-gray-900 mb-3">
                What's your main learning goal?
              </label>
              <textarea
                placeholder="e.g., Get a job in tech, start a side business, learn for fun..."
                value={formData.goals}
                onChange={(e) => setFormData(prev => ({ ...prev, goals: e.target.value }))}
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 outline-none transition-all duration-300 h-24 resize-none"
              />
            </div>

            <div className="mb-8">
              <label className="block text-lg font-semibold text-gray-900 mb-3">
                How much time can you dedicate daily?
              </label>
              <div className="grid grid-cols-2 gap-3">
                {timeCommitments.map((time) => (
                  <div
                    key={time}
                    onClick={() => setFormData(prev => ({ ...prev, timeCommitment: time }))}
                    className={`p-4 border-2 rounded-xl cursor-pointer text-center transition-all duration-300 ${
                      formData.timeCommitment === time
                        ? 'border-indigo-500 bg-indigo-50 text-indigo-700'
                        : 'border-gray-200 hover:border-indigo-300'
                    }`}
                  >
                    {time}
                  </div>
                ))}
              </div>
            </div>

            <div className="flex gap-4">
              <button
                onClick={() => setStep(3)}
                className="flex-1 border-2 border-gray-300 text-gray-700 px-6 py-3 rounded-xl font-semibold hover:bg-gray-50 transition-colors duration-300"
              >
                Back
              </button>
              <button
                onClick={handleComplete}
                disabled={!formData.goals.trim() || !formData.timeCommitment}
                className="flex-1 bg-gradient-to-r from-green-600 to-emerald-600 text-white px-6 py-3 rounded-xl font-semibold disabled:opacity-50 disabled:cursor-not-allowed hover:from-green-700 hover:to-emerald-700 transition-all duration-300"
              >
                Complete Setup 🚀
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Onboarding;
