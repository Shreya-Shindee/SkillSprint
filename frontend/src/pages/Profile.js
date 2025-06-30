import React, { useState, useEffect } from 'react';
import { getCurrentUser, getUserXP, getXPHistory, getAllProgress } from '../api';
import XPBar from '../components/XPBar';
import ProgressBar from '../components/ProgressBar';
import LoadingSpinner from '../components/LoadingSpinner';
import PageTransition from '../components/PageTransition';

const Profile = () => {
  const [user, setUser] = useState(null);
  const [xp, setXP] = useState(0);
  const [xpHistory, setXPHistory] = useState([]);
  const [progress, setProgress] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [userResponse, xpResponse, historyResponse, progressResponse] = await Promise.all([
          getCurrentUser(),
          getUserXP(),
          getXPHistory(),
          getAllProgress()
        ]);
        
        setUser(userResponse.data);
        setXP(xpResponse.data);
        setXPHistory(historyResponse.data);
        setProgress(progressResponse.data);
      } catch (err) {
        console.error('Error fetching profile data:', err);
        setError('Failed to load profile data');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Calculate XP for next level
  const nextLevelXP = Math.ceil(xp / 1000) * 1000;
  const level = Math.floor(xp / 1000) + 1;
  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-[60vh]">
        <LoadingSpinner />
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-gradient-to-r from-red-50 to-red-100 border-l-4 border-red-500 text-red-700 p-6 rounded-xl shadow-md mb-6 flex items-start">
        <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 mr-3 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <div>
          <h3 className="font-bold text-lg mb-1">Error</h3>
          <p>{error}</p>
        </div>
      </div>
    );
  }  return (
    <PageTransition>
      <div className="animate-fadeIn">
      <div className="mb-8 relative">
        <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-blue-500 mb-2">Your Profile</h1>
        <p className="text-gray-600">Track your progress and achievements</p>
        <div className="absolute -top-6 -right-6 w-20 h-20 bg-gradient-to-br from-indigo-500 to-purple-500 rounded-full opacity-10"></div>
      </div>

      {/* User Info Card */}
      <div className="bg-white rounded-2xl shadow-lg p-6 mb-8 border border-gray-100 hover:shadow-xl transition-all duration-300 transform relative overflow-hidden">
        <div className="absolute -top-10 -right-10 w-32 h-32 rounded-full bg-gradient-to-br from-blue-500 to-indigo-500 opacity-10"></div>
        <div className="absolute -bottom-12 -left-12 w-32 h-32 rounded-full bg-gradient-to-tr from-purple-500 to-pink-500 opacity-10"></div>
        
        <div className="flex flex-col md:flex-row md:items-center relative z-10">
          <div className="mb-4 md:mb-0 md:mr-8">
            <div className="w-24 h-24 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-full flex items-center justify-center text-2xl font-bold text-white shadow-md transform transition-all duration-300 hover:scale-105">
              {user?.username.charAt(0).toUpperCase()}
            </div>
          </div>
          <div>
            <h2 className="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600">{user?.username}</h2>
            <p className="text-gray-600">{user?.email}</p>
            <div className="mt-3 inline-flex items-center bg-gradient-to-r from-blue-500 to-indigo-600 text-white px-4 py-2 rounded-full text-sm font-medium shadow-sm">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118l-2.799-2.034c-.784-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
              </svg>
              Level {level} Learner
            </div>
          </div>
        </div>
      </div>      {/* XP Progress */}
      <div className="bg-white rounded-2xl shadow-lg p-6 mb-8 border border-gray-100 hover:shadow-xl transition-all duration-300 transform relative overflow-hidden">
        <div className="absolute -top-10 -left-10 w-32 h-32 rounded-full bg-gradient-to-br from-purple-500 to-pink-500 opacity-10"></div>
        
        <h2 className="text-xl font-semibold text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-pink-600 mb-4 flex items-center">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118l-2.799-2.034c-.784-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
          </svg>
          Experience Points
        </h2>
        
        <XPBar currentXP={xp} nextLevelXP={nextLevelXP} />
        
        <div className="mt-8">
          <h3 className="text-lg font-medium text-gray-700 mb-3 flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2 text-indigo-500" viewBox="0 0 20 20" fill="currentColor">
              <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clipRule="evenodd" />
            </svg>
            Recent XP Activity
          </h3>
          
          {xpHistory.length === 0 ? (
            <div className="bg-gray-50 rounded-xl p-4 text-center">
              <p className="text-gray-500 flex flex-col items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-gray-400 mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                </svg>
                No XP activity yet. Start learning to earn XP!
              </p>
            </div>
          ) : (
            <ul className="divide-y divide-gray-200 rounded-xl overflow-hidden bg-gray-50">
              {xpHistory.slice(0, 5).map((transaction) => (
                <li key={transaction.id} className="py-4 px-4 flex justify-between items-center hover:bg-gray-100 transition-colors duration-200">
                  <span className="text-gray-700 flex items-center">
                    <span className="w-2 h-2 rounded-full bg-indigo-500 mr-2"></span>
                    {transaction.description}
                  </span>
                  <span className="font-medium text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-pink-600">+{transaction.amount} XP</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>      {/* Skills Progress */}
      <div className="bg-white rounded-2xl shadow-lg p-6 mb-8 border border-gray-100 hover:shadow-xl transition-all duration-300 transform relative overflow-hidden">
        <div className="absolute -bottom-12 -right-12 w-32 h-32 rounded-full bg-gradient-to-tr from-teal-500 to-emerald-500 opacity-10"></div>
        
        <h2 className="text-xl font-semibold text-transparent bg-clip-text bg-gradient-to-r from-teal-600 to-emerald-600 mb-4 flex items-center">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
          </svg>
          Skills Progress
        </h2>
        
        {progress.length === 0 ? (
          <div className="bg-gray-50 rounded-xl p-6 text-center">
            <p className="text-gray-500 flex flex-col items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-gray-400 mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
              You haven't started any skills yet. Visit the dashboard to begin!
            </p>
          </div>
        ) : (
          <div className="space-y-6">
            {progress.map((item) => (
              <div key={item.id} className="mb-4 bg-white p-5 rounded-xl border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
                <div className="flex justify-between items-center mb-3">
                  <h3 className="font-medium text-gray-700 flex items-center">
                    <span className="w-2 h-2 rounded-full bg-teal-500 mr-2"></span>
                    {item.skill_name || `Skill #${item.skill_id}`}
                  </h3>
                  <span className={`text-sm px-3 py-1 rounded-full shadow-sm ${
                    item.completed 
                      ? 'bg-gradient-to-r from-green-500 to-emerald-600 text-white' 
                      : 'bg-gradient-to-r from-amber-400 to-orange-500 text-white'
                  }`}>
                    {item.completed ? 'Completed' : 'In Progress'}
                  </span>
                </div>
                <ProgressBar percentage={item.progress_percentage} />
              </div>
            ))}
          </div>
        )}
      </div>
      </div>
    </PageTransition>
  );
};

export default Profile;
