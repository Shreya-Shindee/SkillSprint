import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useToast } from '../contexts/ToastContext';
import LoadingSpinner from '../components/LoadingSpinner';

const AISkillCreator = () => {
  const navigate = useNavigate();
  const { addToast } = useToast();
  
  const [skillName, setSkillName] = useState('');
  const [userLevel, setUserLevel] = useState('beginner');
  const [timeAvailable, setTimeAvailable] = useState(10);
  const [learningStyle, setLearningStyle] = useState('balanced');
  const [useAI, setUseAI] = useState(true);
  const [loading, setLoading] = useState(false);
  const [generatedSkill, setGeneratedSkill] = useState(null);

  const handleGenerateSkill = async (e) => {
    e.preventDefault();
    
    if (!skillName.trim()) {
      addToast('Please enter a skill name', 'error');
      return;
    }

    try {
      setLoading(true);
      const token = localStorage.getItem('token');
      
      if (useAI) {
        // Generate complete skill with AI
        const response = await fetch('http://localhost:8000/skills/ai-generate', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            skill_name: skillName,
            user_level: userLevel,
            use_ai: true
          })
        });

        if (response.ok) {
          const result = await response.json();
          setGeneratedSkill(result);
          addToast('Skill generated successfully with AI!', 'success');
        } else {
          throw new Error('Failed to generate skill');
        }
      } else {
        // Use traditional decomposition
        const response = await fetch('http://localhost:8000/skills/decompose', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            skill_name: skillName,
            user_level: userLevel,
            use_ai: false
          })
        });

        if (response.ok) {
          const result = await response.json();
          setGeneratedSkill(result);
          addToast('Skill decomposed successfully!', 'success');
        } else {
          throw new Error('Failed to decompose skill');
        }
      }
    } catch (error) {
      console.error('Error generating skill:', error);
      addToast('Failed to generate skill. Please try again.', 'error');
    } finally {
      setLoading(false);
    }
  };

  const handleStartLearning = () => {
    if (generatedSkill && generatedSkill.skill_id) {
      navigate(`/learning-path/${generatedSkill.skill_id}`);
    }
  };

  const handleCreatePersonalizedPath = async () => {
    try {
      setLoading(true);
      const token = localStorage.getItem('token');
      
      const response = await fetch('http://localhost:8000/skills/learning-path', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          skill_name: skillName,
          time_available_hours: timeAvailable,
          preferred_difficulty: userLevel,
          learning_style: learningStyle
        })
      });

      if (response.ok) {
        const pathResult = await response.json();
        setGeneratedSkill(pathResult);
        addToast('Personalized learning path created!', 'success');
      } else {
        throw new Error('Failed to create personalized path');
      }
    } catch (error) {
      console.error('Error creating personalized path:', error);
      addToast('Failed to create personalized path. Please try again.', 'error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            🤖 AI-Powered Skill Creation
          </h1>
          <p className="text-xl text-gray-600">
            Let our AI create a personalized learning path just for you
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Input Form */}
          <div className="bg-white rounded-xl p-6 border border-gray-200 shadow-sm">
            <h2 className="text-2xl font-semibold text-gray-900 mb-6">Create Your Learning Path</h2>
            
            <form onSubmit={handleGenerateSkill} className="space-y-6">
              {/* Skill Name */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  What would you like to learn?
                </label>
                <input
                  type="text"
                  value={skillName}
                  onChange={(e) => setSkillName(e.target.value)}
                  placeholder="e.g., Machine Learning, React Development, Digital Marketing"
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>

              {/* User Level */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Your Experience Level
                </label>
                <select
                  value={userLevel}
                  onChange={(e) => setUserLevel(e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
                >
                  <option value="beginner">🌱 Beginner - I'm new to this</option>
                  <option value="intermediate">🚀 Intermediate - I have some experience</option>
                  <option value="advanced">⭐ Advanced - I want to deepen my knowledge</option>
                </select>
              </div>

              {/* Learning Style */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Preferred Learning Style
                </label>
                <select
                  value={learningStyle}
                  onChange={(e) => setLearningStyle(e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
                >
                  <option value="visual">👁️ Visual - Videos and diagrams</option>
                  <option value="reading">📚 Reading - Articles and documentation</option>
                  <option value="hands-on">🛠️ Hands-on - Practice and coding</option>
                  <option value="balanced">⚖️ Balanced - Mix of all styles</option>
                </select>
              </div>

              {/* Time Available */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Time Available per Week (hours)
                </label>
                <input
                  type="range"
                  min="1"
                  max="40"
                  value={timeAvailable}
                  onChange={(e) => setTimeAvailable(parseInt(e.target.value))}
                  className="w-full"
                />
                <div className="flex justify-between text-sm text-gray-500">
                  <span>1 hour</span>
                  <span className="font-medium text-indigo-600">{timeAvailable} hours</span>
                  <span>40 hours</span>
                </div>
              </div>

              {/* AI Toggle */}
              <div className="flex items-center space-x-3">
                <input
                  type="checkbox"
                  id="useAI"
                  checked={useAI}
                  onChange={(e) => setUseAI(e.target.checked)}
                  className="h-5 w-5 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                />
                <label htmlFor="useAI" className="text-sm font-medium text-gray-700">
                  🤖 Use AI for enhanced skill generation (recommended)
                </label>
              </div>

              {/* Action Buttons */}
              <div className="space-y-3">
                <button
                  type="submit"
                  disabled={loading}
                  className="w-full bg-indigo-600 text-white py-3 px-6 rounded-lg hover:bg-indigo-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors font-medium"
                >
                  {loading ? (
                    <div className="flex items-center justify-center">
                      <LoadingSpinner size="small" />
                      <span className="ml-2">Generating...</span>
                    </div>
                  ) : (
                    `${useAI ? '🤖 Generate with AI' : '📊 Decompose Skill'}`
                  )}
                </button>

                <button
                  type="button"
                  onClick={handleCreatePersonalizedPath}
                  disabled={loading || !skillName.trim()}
                  className="w-full bg-purple-600 text-white py-3 px-6 rounded-lg hover:bg-purple-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors font-medium"
                >
                  {loading ? (
                    <div className="flex items-center justify-center">
                      <LoadingSpinner size="small" />
                      <span className="ml-2">Creating...</span>
                    </div>
                  ) : (
                    '🎯 Create Personalized Path'
                  )}
                </button>
              </div>
            </form>
          </div>

          {/* Results */}
          <div className="bg-white rounded-xl p-6 border border-gray-200 shadow-sm">
            <h2 className="text-2xl font-semibold text-gray-900 mb-6">Generated Learning Path</h2>
            
            {!generatedSkill ? (
              <div className="text-center py-12">
                <div className="text-6xl mb-4">🎯</div>
                <p className="text-gray-500">
                  Enter a skill name and click generate to see your personalized learning path
                </p>
              </div>
            ) : (
              <div className="space-y-6">
                {/* Skill Header */}
                <div className="bg-gradient-to-r from-indigo-50 to-purple-50 rounded-lg p-4 border border-indigo-200">
                  <h3 className="text-xl font-bold text-gray-900 mb-2">
                    {generatedSkill.skill_name || generatedSkill.name}
                  </h3>
                  {generatedSkill.description && (
                    <p className="text-gray-600 mb-3">{generatedSkill.description}</p>
                  )}
                  <div className="grid grid-cols-2 gap-4 text-sm">
                    <div>
                      <span className="text-gray-500">Difficulty:</span>
                      <span className="ml-2 font-medium text-indigo-600 capitalize">
                        {generatedSkill.difficulty || userLevel}
                      </span>
                    </div>
                    <div>
                      <span className="text-gray-500">Duration:</span>
                      <span className="ml-2 font-medium text-indigo-600">
                        {generatedSkill.estimated_duration || generatedSkill.estimated_completion_time || 'Flexible'}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Subskills */}
                <div>
                  <h4 className="font-semibold text-gray-900 mb-3">Learning Steps:</h4>
                  <div className="space-y-3">
                    {(generatedSkill.subskills || generatedSkill.personalized_subskills || []).map((subskill, index) => (
                      <div key={index} className="flex items-start space-x-3 p-3 bg-gray-50 rounded-lg">
                        <div className="w-8 h-8 bg-indigo-600 text-white rounded-full flex items-center justify-center text-sm font-bold">
                          {index + 1}
                        </div>
                        <div className="flex-1">
                          <h5 className="font-medium text-gray-900">
                            {typeof subskill === 'string' ? subskill : subskill.name}
                          </h5>
                          {typeof subskill === 'object' && subskill.description && (
                            <p className="text-sm text-gray-600 mt-1">{subskill.description}</p>
                          )}
                          {typeof subskill === 'object' && subskill.estimated_hours && (
                            <span className="text-xs text-indigo-600 font-medium">
                              ~{subskill.estimated_hours} hours
                            </span>
                          )}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* AI Features Badge */}
                {useAI && generatedSkill.skill_id && (
                  <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                    <div className="flex items-center">
                      <div className="text-green-600 mr-3">✨</div>
                      <div>
                        <h5 className="font-medium text-green-900">AI-Enhanced Features Included:</h5>
                        <ul className="text-sm text-green-700 mt-1 space-y-1">
                          <li>• Adaptive quiz questions generated</li>
                          <li>• Personalized resource recommendations</li>
                          <li>• Dynamic difficulty adjustment</li>
                          <li>• Progress tracking with insights</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                )}

                {/* Action Button */}
                <button
                  onClick={handleStartLearning}
                  className="w-full bg-green-600 text-white py-3 px-6 rounded-lg hover:bg-green-700 transition-colors font-medium"
                >
                  🚀 Start Learning This Skill
                </button>
              </div>
            )}
          </div>
        </div>

        {/* Back to Dashboard */}
        <div className="text-center mt-8">
          <button
            onClick={() => navigate('/dashboard')}
            className="text-indigo-600 hover:text-indigo-800 font-medium"
          >
            ← Back to Dashboard
          </button>
        </div>
      </div>
    </div>
  );
};

export default AISkillCreator;
