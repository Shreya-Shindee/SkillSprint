import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import Card from '../components/Card';
import Button from '../components/Button';
import SkillCard from '../components/SkillCard';
import XPBar from '../components/XPBar';
import ProgressBar from '../components/ProgressBar';
import AnimatedNumber from '../components/AnimatedNumber';

const LandingPage = () => {
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();
  const [currentTestimonial, setCurrentTestimonial] = useState(0);
  const [dashboardStats, setDashboardStats] = useState({
    totalSkills: 15,
    completedSkills: 7,
    xp: 2450,
    streak: 12
  });

  const testimonials = [
    {
      name: "Sarah Chen",
      role: "Software Engineer",
      company: "TechCorp",
      image: "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=150&h=150&fit=crop&crop=face",
      text: "SkillSprint helped me transition from marketing to tech in just 6 months. The personalized learning paths are incredible!"
    },
    {
      name: "Marcus Johnson",
      role: "Data Scientist",
      company: "DataFlow Inc",
      image: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=face",
      text: "The AI-powered recommendations are spot-on. I've gained more skills in 3 months than I did in the previous year."
    },
    {
      name: "Emily Rodriguez",
      role: "UX Designer",
      company: "DesignLab",
      image: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face",
      text: "The gamification aspect kept me engaged throughout my learning journey. I love earning XP for every milestone!"
    },
    {
      name: "David Park",
      role: "Product Manager",
      company: "Innovation Co",
      image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face",
      text: "SkillSprint's adaptive learning system helped me upskill efficiently while working full-time. Highly recommend!"
    }
  ];

  const features = [
    {
      icon: "🎯",
      title: "Personalized Learning Paths",
      description: "AI-powered recommendations tailored to your goals, experience level, and learning style.",
      highlight: "99% accuracy"
    },
    {
      icon: "🚀",
      title: "Accelerated Progress",
      description: "Advanced learning algorithms that adapt to your pace and optimize retention.",
      highlight: "3x faster"
    },
    {
      icon: "🏆",
      title: "Gamified Experience",
      description: "Earn XP, unlock achievements, and track your progress with engaging challenges.",
      highlight: "Stay motivated"
    },
    {
      icon: "📊",
      title: "Real-time Analytics",
      description: "Detailed insights into your learning patterns, strengths, and areas for improvement.",
      highlight: "Data-driven"
    },
    {
      icon: "🌐",
      title: "Industry-Relevant Skills",
      description: "Curated content from top companies and industry experts to ensure job readiness.",
      highlight: "Market-focused"
    },
    {
      icon: "🤝",
      title: "Community Support",
      description: "Connect with peers, mentors, and experts in your field for collaborative learning.",
      highlight: "Network & grow"
    }
  ];

  const steps = [
    {
      number: "01",
      title: "Assessment",
      description: "Take our comprehensive skill assessment to identify your current level and learning goals.",
      icon: "📋"
    },
    {
      number: "02",
      title: "Personalization",
      description: "Our AI creates a customized learning path with resources, projects, and milestones.",
      icon: "🎯"
    },
    {
      number: "03",
      title: "Achievement",
      description: "Learn, practice, and showcase your new skills with real-world projects and certifications.",
      icon: "🏆"
    }
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTestimonial((prev) => (prev + 1) % testimonials.length);
    }, 4000); // More reasonable 4 second interval
    return () => clearInterval(interval);
  }, [testimonials.length]);

  const handleGetStarted = () => {
    if (isAuthenticated) {
      navigate('/dashboard');
    } else {
      navigate('/onboarding');
    }
  };

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-800">
      {/* Hero Section */}
      <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
        {/* Animated Background Elements */}
        <div className="absolute inset-0">
          <div className="absolute top-20 left-10 w-72 h-72 bg-blue-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob"></div>
          <div className="absolute top-40 right-10 w-72 h-72 bg-yellow-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-2000"></div>
          <div className="absolute -bottom-8 left-20 w-72 h-72 bg-pink-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-4000"></div>
        </div>

        <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="space-y-8">
            <h1 className="text-5xl md:text-7xl font-bold text-white leading-tight">
              Accelerate Your
              <span className="block bg-gradient-to-r from-cyan-400 to-violet-400 bg-clip-text text-transparent animate-pulse">
                Journey
              </span>
            </h1>
            
            <p className="text-xl md:text-2xl text-gray-300 max-w-3xl mx-auto leading-relaxed">
              Transform your career with AI-powered learning paths, personalized challenges, 
              and real-world projects that adapt to your pace and goals.
            </p>

            <div className="flex flex-col sm:flex-row gap-6 justify-center items-center">
              <Button
                onClick={handleGetStarted}
                className="px-8 py-4 bg-gradient-to-r from-cyan-500 to-violet-500 hover:from-cyan-600 hover:to-violet-600 text-white font-semibold rounded-xl shadow-2xl transform hover:scale-105 transition-all duration-300 text-lg"
              >
                {isAuthenticated ? 'Go to Dashboard' : 'Start Your Journey'}
              </Button>
              
              <Button
                onClick={() => scrollToSection('features')}
                className="px-8 py-4 bg-white/10 backdrop-blur-md hover:bg-white/20 text-white font-semibold rounded-xl border border-white/20 transition-all duration-300 text-lg"
              >
                Explore Features
              </Button>
            </div>

            {/* Stats Row */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-8 mt-16">
              <div className="text-center">
                <div className="text-3xl md:text-4xl font-bold text-cyan-400">
                  <AnimatedNumber end={50000} duration={2000} />+
                </div>
                <div className="text-gray-300">Active Learners</div>
              </div>
              <div className="text-center">
                <div className="text-3xl md:text-4xl font-bold text-violet-400">
                  <AnimatedNumber end={500} duration={2000} />+
                </div>
                <div className="text-gray-300">Skill Paths</div>
              </div>
              <div className="text-center">
                <div className="text-3xl md:text-4xl font-bold text-pink-400">
                  <AnimatedNumber end={95} duration={2000} />%
                </div>
                <div className="text-gray-300">Success Rate</div>
              </div>
              <div className="text-center">
                <div className="text-3xl md:text-4xl font-bold text-yellow-400">
                  <AnimatedNumber end={1000} duration={2000} />+
                </div>
                <div className="text-gray-300">Companies</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Interactive Dashboard Preview Section */}
      <section className="py-24 bg-gradient-to-r from-gray-50 to-gray-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-5xl font-bold text-gray-900 mb-6">
              See SkillSprint in Action
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Experience our interactive dashboard preview below and discover how we transform learning into an engaging, measurable journey.
            </p>
          </div>

          <div className="bg-white rounded-3xl shadow-2xl p-8 max-w-6xl mx-auto transform hover:scale-105 transition-all duration-300">
            <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
              <div className="bg-gradient-to-br from-cyan-500/20 to-blue-500/20 p-6 rounded-2xl border border-cyan-500/20 transform hover:scale-105 transition-all duration-300 hover:shadow-xl">
                <div className="flex items-center justify-between mb-4">
                  <h3 className="text-gray-800 font-semibold">Total Skills</h3>
                  <span className="text-3xl animate-bounce">🎯</span>
                </div>
                <div className="text-4xl font-bold text-cyan-600 mb-1">
                  <AnimatedNumber end={dashboardStats.totalSkills} duration={2000} />
                </div>
                <div className="text-sm text-gray-600">Skills Available</div>
                <div className="text-xs text-cyan-500 mt-1">📈 Growing daily</div>
              </div>

              <div className="bg-gradient-to-br from-violet-500/20 to-purple-500/20 p-6 rounded-2xl border border-violet-500/20 transform hover:scale-105 transition-all duration-300 hover:shadow-xl">
                <div className="flex items-center justify-between mb-4">
                  <h3 className="text-gray-800 font-semibold">Completed</h3>
                  <span className="text-3xl animate-pulse">✅</span>
                </div>
                <div className="text-4xl font-bold text-violet-600 mb-1">
                  <AnimatedNumber end={dashboardStats.completedSkills} duration={2000} />
                </div>
                <div className="text-sm text-gray-600">Skills Mastered</div>
                <div className="text-xs text-violet-500 mt-1">🏆 Expert level</div>
              </div>

              <div className="bg-gradient-to-br from-pink-500/20 to-rose-500/20 p-6 rounded-2xl border border-pink-500/20 transform hover:scale-105 transition-all duration-300 hover:shadow-xl">
                <div className="flex items-center justify-between mb-4">
                  <h3 className="text-gray-800 font-semibold">Total XP</h3>
                  <span className="text-3xl animate-spin">⭐</span>
                </div>
                <div className="text-4xl font-bold text-pink-600 mb-1">
                  <AnimatedNumber end={dashboardStats.xp} duration={2000} />
                </div>
                <div className="text-sm text-gray-600">Experience Points</div>
                <div className="text-xs text-pink-500 mt-1">⚡ Level 18</div>
              </div>

              <div className="bg-gradient-to-br from-yellow-500/20 to-orange-500/20 p-6 rounded-2xl border border-yellow-500/20 transform hover:scale-105 transition-all duration-300 hover:shadow-xl">
                <div className="flex items-center justify-between mb-4">
                  <h3 className="text-gray-800 font-semibold">Day Streak</h3>
                  <span className="text-3xl animate-pulse">🔥</span>
                </div>
                <div className="text-4xl font-bold text-yellow-600 mb-1">
                  <AnimatedNumber end={dashboardStats.streak} duration={2000} />
                </div>
                <div className="text-sm text-gray-600">Learning Streak</div>
                <div className="text-xs text-yellow-500 mt-1">🔥 On fire!</div>
              </div>
            </div>

            {/* Enhanced Progress Section with Animations */}
            <div className="grid md:grid-cols-2 gap-8">
              <div className="bg-gradient-to-br from-indigo-50 to-blue-50 p-6 rounded-2xl">
                <h4 className="text-xl font-semibold text-gray-800 mb-6">Active Learning Paths</h4>
                <div className="space-y-4">
                  <div className="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition-shadow duration-300">
                    <div className="flex justify-between items-center mb-2">
                      <span className="font-medium text-gray-800">React Development</span>
                      <span className="text-sm text-gray-500">10/12 completed</span>
                    </div>
                    <div className="w-full bg-gray-200 rounded-full h-3 mb-2">
                      <div 
                        className="h-3 rounded-full bg-gradient-to-r from-blue-400 to-blue-600 transition-all duration-1000 ease-out animate-pulse"
                        style={{ width: '85%' }}
                      ></div>
                    </div>
                    <div className="flex justify-between text-xs text-gray-500">
                      <span>85% complete</span>
                      <span>Est. 1 week remaining</span>
                    </div>
                  </div>

                  <div className="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition-shadow duration-300">
                    <div className="flex justify-between items-center mb-2">
                      <span className="font-medium text-gray-800">Python Fundamentals</span>
                      <span className="text-sm text-gray-500">9/15 completed</span>
                    </div>
                    <div className="w-full bg-gray-200 rounded-full h-3 mb-2">
                      <div 
                        className="h-3 rounded-full bg-gradient-to-r from-green-400 to-green-600 transition-all duration-1000 ease-out"
                        style={{ width: '60%' }}
                      ></div>
                    </div>
                    <div className="flex justify-between text-xs text-gray-500">
                      <span>60% complete</span>
                      <span>Est. 2-3 weeks remaining</span>
                    </div>
                  </div>

                  <div className="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition-shadow duration-300">
                    <div className="flex justify-between items-center mb-2">
                      <span className="font-medium text-gray-800">UI/UX Design</span>
                      <span className="text-sm text-gray-500">8/20 completed</span>
                    </div>
                    <div className="w-full bg-gray-200 rounded-full h-3 mb-2">
                      <div 
                        className="h-3 rounded-full bg-gradient-to-r from-purple-400 to-purple-600 transition-all duration-1000 ease-out"
                        style={{ width: '40%' }}
                      ></div>
                    </div>
                    <div className="flex justify-between text-xs text-gray-500">
                      <span>40% complete</span>
                      <span>Est. 4 weeks remaining</span>
                    </div>
                  </div>
                </div>
              </div>
              
              <div className="bg-gradient-to-br from-purple-50 to-indigo-50 p-6 rounded-2xl">
                <h4 className="text-xl font-semibold text-gray-800 mb-6">Recent Achievements</h4>
                <XPBar currentXP={2450} nextLevel={3000} level={8} />
                
                <div className="mt-6 space-y-3">
                  <div className="flex items-center justify-between p-3 bg-yellow-50 rounded-lg transform hover:scale-105 transition-all duration-300">
                    <div className="flex items-center gap-3">
                      <span className="text-2xl animate-bounce">🏆</span>
                      <div>
                        <div className="font-medium text-gray-800">React Hooks Master</div>
                        <div className="text-xs text-gray-500">2 days ago</div>
                      </div>
                    </div>
                    <div className="text-orange-600 font-semibold animate-pulse">+250 XP</div>
                  </div>

                  <div className="flex items-center justify-between p-3 bg-blue-50 rounded-lg transform hover:scale-105 transition-all duration-300">
                    <div className="flex items-center gap-3">
                      <span className="text-2xl animate-bounce">🏆</span>
                      <div>
                        <div className="font-medium text-gray-800">API Integration Pro</div>
                        <div className="text-xs text-gray-500">5 days ago</div>
                      </div>
                    </div>
                    <div className="text-blue-600 font-semibold animate-pulse">+200 XP</div>
                  </div>

                  <div className="flex items-center justify-between p-3 bg-green-50 rounded-lg transform hover:scale-105 transition-all duration-300">
                    <div className="flex items-center gap-3">
                      <span className="text-2xl animate-bounce">🔥</span>
                      <div>
                        <div className="font-medium text-gray-800">7-Day Streak</div>
                        <div className="text-xs text-gray-500">1 week ago</div>
                      </div>
                    </div>
                    <div className="text-green-600 font-semibold animate-pulse">+100 XP</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
              Why Choose SkillSprint?
            </h2>
            <p className="text-xl text-gray-300 max-w-3xl mx-auto">
              Experience the future of learning with our cutting-edge features designed to maximize your growth.
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <Card
                key={index}
                className="bg-white/5 backdrop-blur-xl border border-white/10 p-8 hover:bg-white/10 transition-all duration-300 transform hover:scale-105 hover:rotate-1"
              >
                <div className="text-4xl mb-4">{feature.icon}</div>
                <h3 className="text-xl font-bold text-white mb-3">{feature.title}</h3>
                <p className="text-gray-300 mb-4">{feature.description}</p>
                <div className="inline-block px-3 py-1 bg-gradient-to-r from-cyan-500/20 to-violet-500/20 rounded-full text-sm text-cyan-400 border border-cyan-500/30">
                  {feature.highlight}
                </div>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section className="py-20 bg-black/20 backdrop-blur-md">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
              Your Journey in 3 Steps
            </h2>
            <p className="text-xl text-gray-300 max-w-3xl mx-auto">
              Get started with SkillSprint in minutes and begin your transformation today.
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {steps.map((step, index) => (
              <div
                key={index}
                className="relative text-center"
              >
                <div className="mb-8">
                  <div className="w-20 h-20 bg-gradient-to-br from-cyan-500 to-violet-500 rounded-full flex items-center justify-center mx-auto mb-4 text-2xl transform hover:scale-110 transition-transform duration-300">
                    {step.icon}
                  </div>
                  <div className="text-6xl font-bold text-white/10 absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-4 z-0">
                    {step.number}
                  </div>
                </div>
                
                <h3 className="text-2xl font-bold text-white mb-4 relative z-10">{step.title}</h3>
                <p className="text-gray-300 relative z-10">{step.description}</p>
                
                {index < steps.length - 1 && (
                  <div className="hidden md:block absolute top-10 left-full w-full h-0.5 bg-gradient-to-r from-cyan-500 to-violet-500 transform -translate-y-1/2 z-0"></div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials Section - Circular Rotating Cards */}
      <section className="py-24 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-20">
            <h2 className="text-5xl font-bold text-gray-900 mb-6">
              Learned by Learners Worldwide
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Join thousands of successful learners who have transformed their careers with SkillSprint. Here are their stories.
            </p>
          </div>

          {/* Enhanced Testimonials Carousel */}
          <div className="relative max-w-4xl mx-auto">
            {/* Main testimonial card */}
            <div className="bg-white rounded-3xl shadow-2xl p-8 border border-gray-100 min-h-[300px] transform transition-all duration-500 hover:scale-105">
              <div className="flex flex-col md:flex-row items-center gap-8">
                {/* Profile image */}
                <div className="flex-shrink-0">
                  <img 
                    src={testimonials[currentTestimonial].image} 
                    alt={testimonials[currentTestimonial].name}
                    className="w-24 h-24 rounded-full object-cover border-4 border-indigo-200 shadow-lg"
                  />
                </div>
                
                {/* Content */}
                <div className="flex-1 text-center md:text-left">
                  {/* Stars */}
                  <div className="flex justify-center md:justify-start mb-4">
                    {[...Array(5)].map((_, i) => (
                      <span key={i} className="text-yellow-400 text-xl animate-pulse" style={{ animationDelay: `${i * 0.1}s` }}>⭐</span>
                    ))}
                  </div>
                  
                  {/* Quote */}
                  <p className="text-gray-700 text-lg leading-relaxed mb-6 italic">
                    "{testimonials[currentTestimonial].text}"
                  </p>
                  
                  {/* Author info */}
                  <div>
                    <h4 className="font-bold text-gray-900 text-xl">{testimonials[currentTestimonial].name}</h4>
                    <p className="text-gray-600">{testimonials[currentTestimonial].role}</p>
                    <p className="text-indigo-600 font-medium">{testimonials[currentTestimonial].company}</p>
                  </div>
                </div>
              </div>
            </div>
            
            {/* Navigation buttons */}
            <button
              onClick={() => setCurrentTestimonial((prev) => (prev - 1 + testimonials.length) % testimonials.length)}
              className="absolute left-4 top-1/2 transform -translate-y-1/2 bg-white/90 backdrop-blur-sm border border-gray-200 rounded-full p-3 shadow-lg hover:bg-white hover:scale-110 transition-all duration-300"
            >
              <svg className="w-6 h-6 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
            </button>
            
            <button
              onClick={() => setCurrentTestimonial((prev) => (prev + 1) % testimonials.length)}
              className="absolute right-4 top-1/2 transform -translate-y-1/2 bg-white/90 backdrop-blur-sm border border-gray-200 rounded-full p-3 shadow-lg hover:bg-white hover:scale-110 transition-all duration-300"
            >
              <svg className="w-6 h-6 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </button>
            
            {/* Progress indicators */}
            <div className="flex justify-center mt-8 gap-2">
              {testimonials.map((_, index) => (
                <button
                  key={index}
                  onClick={() => setCurrentTestimonial(index)}
                  className={`w-3 h-3 rounded-full transition-all duration-300 ${
                    index === currentTestimonial 
                      ? 'bg-indigo-600 scale-125' 
                      : 'bg-gray-300 hover:bg-gray-400'
                  }`}
                />
              ))}
            </div>
            
            {/* Mini preview cards */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-8">
              {testimonials.map((testimonial, index) => (
                <button
                  key={index}
                  onClick={() => setCurrentTestimonial(index)}
                  className={`p-4 rounded-xl border transition-all duration-300 transform hover:scale-105 ${
                    index === currentTestimonial
                      ? 'border-indigo-300 bg-indigo-50 shadow-lg'
                      : 'border-gray-200 bg-white hover:border-indigo-200 hover:shadow-md'
                  }`}
                >
                  <img 
                    src={testimonial.image} 
                    alt={testimonial.name}
                    className="w-12 h-12 rounded-full object-cover mx-auto mb-2 border-2 border-gray-200"
                  />
                  <h5 className="font-semibold text-sm text-gray-800 truncate">{testimonial.name}</h5>
                  <p className="text-xs text-gray-500 truncate">{testimonial.role}</p>
                </button>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-cyan-600/20 to-violet-600/20 backdrop-blur-md">
        <div className="max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
            Ready to Sprint Ahead?
          </h2>
          <p className="text-xl text-gray-300 mb-8 max-w-2xl mx-auto">
            Join thousands of learners who are accelerating their careers with personalized, 
            AI-powered learning experiences.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-6 justify-center items-center">
            <Button
              onClick={handleGetStarted}
              className="px-8 py-4 bg-gradient-to-r from-cyan-500 to-violet-500 hover:from-cyan-600 hover:to-violet-600 text-white font-semibold rounded-xl shadow-2xl transform hover:scale-105 transition-all duration-300 text-lg"
            >
              {isAuthenticated ? 'Continue Learning' : 'Start Free Today'}
            </Button>
            
            <div className="text-gray-300 text-sm">
              ✨ No credit card required • 7-day free trial
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-black/40 backdrop-blur-md py-12 border-t border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <h3 className="text-2xl font-bold bg-gradient-to-r from-cyan-400 to-violet-400 bg-clip-text text-transparent mb-4">
                SkillSprint
              </h3>
              <p className="text-gray-400 mb-4">
                Accelerate your learning journey with AI-powered personalization.
              </p>
              <div className="flex space-x-4">
                <a href="#" className="text-gray-400 hover:text-cyan-400 transition-colors">
                  <span className="sr-only">Twitter</span>
                  🐦
                </a>
                <a href="#" className="text-gray-400 hover:text-cyan-400 transition-colors">
                  <span className="sr-only">LinkedIn</span>
                  💼
                </a>
                <a href="#" className="text-gray-400 hover:text-cyan-400 transition-colors">
                  <span className="sr-only">GitHub</span>
                  🐱
                </a>
              </div>
            </div>

            <div>
              <h4 className="text-white font-semibold mb-4">Product</h4>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white transition-colors">Features</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Pricing</a></li>
                <li><a href="#" className="hover:text-white transition-colors">API</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Integrations</a></li>
              </ul>
            </div>

            <div>
              <h4 className="text-white font-semibold mb-4">Resources</h4>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white transition-colors">Documentation</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Help Center</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Blog</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Community</a></li>
              </ul>
            </div>

            <div>
              <h4 className="text-white font-semibold mb-4">Company</h4>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white transition-colors">About</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Careers</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Privacy</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Terms</a></li>
              </ul>
            </div>
          </div>

          <div className="border-t border-white/10 mt-8 pt-8 text-center text-gray-400">
            <p>&copy; 2024 SkillSprint. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;
