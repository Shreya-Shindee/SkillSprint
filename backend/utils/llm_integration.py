"""
LLM Integration for AI-Powered Skill Decomposition and Quiz Generation
Supports multiple LLM providers: OpenAI, Gemini, and local models
"""

import json
import os
import requests
from typing import List, Dict, Any, Optional
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMIntegration:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.gemini_api_key = os.getenv('GEMINI_API_KEY')
        
    def decompose_skill_with_llm(self, skill_name: str, user_level: str = "beginner") -> Dict[str, Any]:
        """
        Use LLM to decompose a skill into a structured learning path
        
        Args:
            skill_name: The skill to decompose
            user_level: beginner, intermediate, or advanced
            
        Returns:
            Dict containing structured skill decomposition
        """
        prompt = f"""
        Create a comprehensive learning roadmap for "{skill_name}" for a {user_level} level learner.
        
        Break down the skill into 5-8 logical subskills that build upon each other.
        Each subskill should be specific and actionable.
        
        Return the response as a JSON object with this exact structure:
        {{
            "name": "{skill_name}",
            "description": "Brief description of the skill",
            "difficulty": "{user_level}",
            "estimated_duration": "X weeks",
            "subskills": [
                {{
                    "name": "Subskill 1 Name",
                    "description": "What this subskill covers",
                    "order": 1,
                    "estimated_hours": 10,
                    "prerequisites": []
                }},
                ...
            ]
        }}
        
        Make sure the subskills follow a logical learning progression.
        """
        
        try:
            # Try Gemini first (free tier available)
            if self.gemini_api_key:
                return self._call_gemini(prompt)
            # Fallback to OpenAI
            elif self.openai_api_key:
                return self._call_openai(prompt)
            else:
                logger.warning("No LLM API keys found, using fallback method")
                return self._fallback_decomposition(skill_name, user_level)
                
        except Exception as e:
            logger.error(f"LLM call failed: {str(e)}")
            return self._fallback_decomposition(skill_name, user_level)
    
    def generate_quiz_questions(self, subskill_name: str, num_questions: int = 5) -> List[Dict[str, Any]]:
        """
        Generate quiz questions for a specific subskill using LLM
        
        Args:
            subskill_name: The subskill to create questions for
            num_questions: Number of questions to generate
            
        Returns:
            List of quiz questions with multiple choice answers
        """
        prompt = f"""
        Generate {num_questions} multiple choice quiz questions for the topic: "{subskill_name}"
        
        Each question should:
        - Test practical understanding, not just memorization
        - Have 4 options (A, B, C, D)
        - Have exactly one correct answer
        - Include a brief explanation for the correct answer
        
        Return the response as a JSON array with this exact structure:
        [
            {{
                "question": "Question text here?",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": "Option B",
                "explanation": "Brief explanation of why this is correct",
                "difficulty": "easy/medium/hard"
            }},
            ...
        ]
        """
        
        try:
            if self.gemini_api_key:
                result = self._call_gemini(prompt)
                if isinstance(result, list):
                    return result
                return result.get('questions', [])
            elif self.openai_api_key:
                result = self._call_openai(prompt)
                if isinstance(result, list):
                    return result
                return result.get('questions', [])
            else:
                return self._fallback_quiz_questions(subskill_name, num_questions)
                
        except Exception as e:
            logger.error(f"Quiz generation failed: {str(e)}")
            return self._fallback_quiz_questions(subskill_name, num_questions)
    
    def _call_gemini(self, prompt: str) -> Dict[str, Any]:
        """Call Google Gemini API"""
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.gemini_api_key}"
        
        headers = {
            'Content-Type': 'application/json',
        }
        
        data = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }]
        }
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        text_content = result['candidates'][0]['content']['parts'][0]['text']
        
        # Extract JSON from the response
        try:
            # Try to find JSON in the response
            start = text_content.find('{')
            end = text_content.rfind('}') + 1
            if start != -1 and end != 0:
                json_str = text_content[start:end]
                return json.loads(json_str)
            else:
                # Try to find JSON array
                start = text_content.find('[')
                end = text_content.rfind(']') + 1
                if start != -1 and end != 0:
                    json_str = text_content[start:end]
                    return json.loads(json_str)
        except json.JSONDecodeError:
            logger.error("Failed to parse JSON from Gemini response")
            
        return {"error": "Failed to parse LLM response"}
    
    def _call_openai(self, prompt: str) -> Dict[str, Any]:
        """Call OpenAI API"""
        url = "https://api.openai.com/v1/chat/completions"
        
        headers = {
            'Authorization': f'Bearer {self.openai_api_key}',
            'Content-Type': 'application/json',
        }
        
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are an expert educational content creator. Always return valid JSON."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        content = result['choices'][0]['message']['content']
        
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            logger.error("Failed to parse JSON from OpenAI response")
            return {"error": "Failed to parse LLM response"}
    
    def _fallback_decomposition(self, skill_name: str, user_level: str) -> Dict[str, Any]:
        """Fallback skill decomposition when LLM is not available"""
        
        # Common skill patterns
        if "python" in skill_name.lower():
            subskills = [
                {"name": "Python Syntax and Variables", "description": "Basic syntax, variables, and data types", "order": 1, "estimated_hours": 8},
                {"name": "Control Flow", "description": "If statements, loops, and conditional logic", "order": 2, "estimated_hours": 6},
                {"name": "Functions and Modules", "description": "Creating and using functions, importing modules", "order": 3, "estimated_hours": 8},
                {"name": "Data Structures", "description": "Lists, dictionaries, sets, and tuples", "order": 4, "estimated_hours": 10},
                {"name": "Object-Oriented Programming", "description": "Classes, objects, inheritance", "order": 5, "estimated_hours": 12},
                {"name": "File Handling and APIs", "description": "Working with files and web APIs", "order": 6, "estimated_hours": 8},
            ]
        elif "web" in skill_name.lower() or "html" in skill_name.lower():
            subskills = [
                {"name": "HTML Fundamentals", "description": "Basic HTML structure and tags", "order": 1, "estimated_hours": 6},
                {"name": "CSS Styling", "description": "Styling and layout with CSS", "order": 2, "estimated_hours": 10},
                {"name": "JavaScript Basics", "description": "Variables, functions, and DOM manipulation", "order": 3, "estimated_hours": 12},
                {"name": "Responsive Design", "description": "Mobile-first design and media queries", "order": 4, "estimated_hours": 8},
                {"name": "Modern JavaScript", "description": "ES6+, async/await, and modern patterns", "order": 5, "estimated_hours": 10},
                {"name": "Web Frameworks", "description": "Introduction to popular frameworks", "order": 6, "estimated_hours": 15},
            ]
        else:
            # Generic decomposition
            subskills = [
                {"name": f"{skill_name} Fundamentals", "description": f"Core concepts and basics of {skill_name}", "order": 1, "estimated_hours": 10},
                {"name": f"Intermediate {skill_name}", "description": f"Building on the basics", "order": 2, "estimated_hours": 12},
                {"name": f"Practical {skill_name}", "description": f"Hands-on practice and projects", "order": 3, "estimated_hours": 15},
                {"name": f"Advanced {skill_name}", "description": f"Advanced concepts and techniques", "order": 4, "estimated_hours": 18},
                {"name": f"{skill_name} Best Practices", "description": f"Industry standards and best practices", "order": 5, "estimated_hours": 8},
            ]
        
        return {
            "name": skill_name,
            "description": f"Comprehensive learning path for {skill_name}",
            "difficulty": user_level,
            "estimated_duration": f"{sum(s['estimated_hours'] for s in subskills) // 10} weeks",
            "subskills": subskills
        }
    
    def _fallback_quiz_questions(self, subskill_name: str, num_questions: int) -> List[Dict[str, Any]]:
        """Fallback quiz questions when LLM is not available"""
        # This could be enhanced with a local question bank
        return [
            {
                "question": f"What is the most important concept in {subskill_name}?",
                "options": [
                    "Understanding the fundamentals",
                    "Memorizing syntax",
                    "Speed of execution",
                    "Tool selection"
                ],
                "correct_answer": "Understanding the fundamentals",
                "explanation": "Strong fundamentals provide the foundation for advanced learning.",
                "difficulty": "easy"
            },
            {
                "question": f"When learning {subskill_name}, what should you prioritize?",
                "options": [
                    "Theory only",
                    "Practice only", 
                    "Balance of theory and practice",
                    "Following tutorials exactly"
                ],
                "correct_answer": "Balance of theory and practice",
                "explanation": "Combining theoretical understanding with practical application leads to better learning outcomes.",
                "difficulty": "medium"
            }
        ][:num_questions]

# Global instance
llm_integration = LLMIntegration()
