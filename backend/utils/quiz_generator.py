"""
Quiz Generation and Management System
Handles AI-powered quiz generation, question banking, and adaptive difficulty
"""

import random
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from database.database import get_db
from models.models import QuizQuestion, QuizAttempt, Skill, User
from utils.llm_integration import llm_integration
import logging

logger = logging.getLogger(__name__)

class QuizManager:
    def __init__(self):
        self.difficulty_weights = {
            "easy": 1.0,
            "medium": 1.5, 
            "hard": 2.0
        }
    
    def generate_skill_quiz(self, skill_id: int, user_id: int, num_questions: int = 5, db: Session = None) -> Dict[str, Any]:
        """
        Generate a quiz for a specific skill, adapting difficulty based on user progress
        
        Args:
            skill_id: The skill to generate quiz for
            user_id: The user taking the quiz
            num_questions: Number of questions to include
            db: Database session
            
        Returns:
            Dict containing quiz questions and metadata
        """
        if not db:
            db = next(get_db())
        
        try:
            # Get the skill details
            skill = db.query(Skill).filter(Skill.id == skill_id).first()
            if not skill:
                raise ValueError(f"Skill with id {skill_id} not found")
            
            # Determine user's skill level based on progress
            user_level = self._get_user_skill_level(user_id, skill_id, db)
            
            # Get existing questions from database
            existing_questions = db.query(QuizQuestion).filter(
                QuizQuestion.skill_id == skill_id
            ).all()
            
            quiz_questions = []
            
            # If we have enough existing questions, use them
            if len(existing_questions) >= num_questions:
                # Select questions based on difficulty and subskills
                selected_questions = self._select_adaptive_questions(
                    existing_questions, user_level, num_questions, user_id, db
                )
                quiz_questions = [self._format_question(q) for q in selected_questions]
            else:
                # Generate new questions using AI if we don't have enough
                needed_questions = num_questions - len(existing_questions)
                
                # Use existing questions first
                quiz_questions.extend([self._format_question(q) for q in existing_questions])
                
                # Generate new questions for subskills
                if skill.subskills:
                    for subskill in skill.subskills[:needed_questions]:
                        new_questions = self._generate_questions_for_subskill(
                            skill_id, subskill, user_level, db
                        )
                        quiz_questions.extend(new_questions[:1])  # Add one question per subskill
                
                # If still need more questions, generate general skill questions
                if len(quiz_questions) < num_questions:
                    general_questions = self._generate_questions_for_subskill(
                        skill_id, skill.name, user_level, db
                    )
                    quiz_questions.extend(general_questions[:num_questions - len(quiz_questions)])
            
            # Randomize question order
            random.shuffle(quiz_questions)
            
            # Limit to requested number
            quiz_questions = quiz_questions[:num_questions]
            
            return {
                "skill_id": skill_id,
                "skill_name": skill.name,
                "questions": quiz_questions,
                "total_questions": len(quiz_questions),
                "estimated_time_minutes": len(quiz_questions) * 2,  # 2 minutes per question
                "difficulty_level": user_level
            }
            
        except Exception as e:
            logger.error(f"Error generating quiz for skill {skill_id}: {str(e)}")
            return self._fallback_quiz(skill_id, num_questions, db)
    
    def submit_quiz_attempt(self, user_id: int, skill_id: int, questions: List[Dict], 
                           user_answers: List[str], time_taken: int, db: Session) -> Dict[str, Any]:
        """
        Process and save a quiz attempt, calculate score and provide feedback
        
        Args:
            user_id: User taking the quiz
            skill_id: Skill being tested
            questions: List of questions asked
            user_answers: List of user's answers
            time_taken: Time taken in seconds
            db: Database session
            
        Returns:
            Dict containing results and feedback
        """
        try:
            # Calculate score
            correct_answers = 0
            feedback = []
            
            for i, (question, user_answer) in enumerate(zip(questions, user_answers)):
                is_correct = user_answer == question.get('correct_answer')
                if is_correct:
                    correct_answers += 1
                
                feedback.append({
                    "question_number": i + 1,
                    "question": question.get('question'),
                    "user_answer": user_answer,
                    "correct_answer": question.get('correct_answer'),
                    "is_correct": is_correct,
                    "explanation": question.get('explanation')
                })
            
            score_percentage = (correct_answers / len(questions)) * 100
            
            # Save quiz attempt to database
            quiz_attempt = QuizAttempt(
                user_id=user_id,
                skill_id=skill_id,
                questions_data=questions,
                user_answers=user_answers,
                score=correct_answers,
                total_questions=len(questions),
                time_taken_seconds=time_taken
            )
            
            db.add(quiz_attempt)
            db.commit()
            
            # Update user's skill progress
            self._update_skill_progress_from_quiz(user_id, skill_id, score_percentage, db)
            
            # Award XP based on performance
            xp_earned = self._calculate_quiz_xp(correct_answers, len(questions), time_taken)
            if xp_earned > 0:
                self._award_xp(user_id, xp_earned, "quiz_completion", skill_id, db)
            
            return {
                "score": correct_answers,
                "total_questions": len(questions),
                "score_percentage": score_percentage,
                "time_taken_seconds": time_taken,
                "xp_earned": xp_earned,
                "feedback": feedback,
                "performance_level": self._get_performance_level(score_percentage),
                "recommendations": self._get_quiz_recommendations(score_percentage, feedback)
            }
            
        except Exception as e:
            logger.error(f"Error processing quiz attempt: {str(e)}")
            db.rollback()
            raise
    
    def _get_user_skill_level(self, user_id: int, skill_id: int, db: Session) -> str:
        """Determine user's skill level based on their progress and quiz history"""
        # Get recent quiz attempts
        recent_attempts = db.query(QuizAttempt).filter(
            QuizAttempt.user_id == user_id,
            QuizAttempt.skill_id == skill_id
        ).order_by(QuizAttempt.completed_at.desc()).limit(3).all()
        
        if not recent_attempts:
            return "beginner"
        
        # Calculate average score from recent attempts
        avg_score = sum(attempt.score / attempt.total_questions for attempt in recent_attempts) / len(recent_attempts)
        
        if avg_score >= 0.8:
            return "advanced"
        elif avg_score >= 0.6:
            return "intermediate"
        else:
            return "beginner"
    
    def _select_adaptive_questions(self, questions: List[QuizQuestion], user_level: str, 
                                 num_questions: int, user_id: int, db: Session) -> List[QuizQuestion]:
        """Select questions adaptively based on user level and performance"""
        # Separate questions by difficulty
        easy_questions = [q for q in questions if q.difficulty == "easy"]
        medium_questions = [q for q in questions if q.difficulty == "medium"]
        hard_questions = [q for q in questions if q.difficulty == "hard"]
        
        # Determine question distribution based on user level
        if user_level == "beginner":
            distribution = {"easy": 0.6, "medium": 0.3, "hard": 0.1}
        elif user_level == "intermediate":
            distribution = {"easy": 0.3, "medium": 0.5, "hard": 0.2}
        else:  # advanced
            distribution = {"easy": 0.2, "medium": 0.3, "hard": 0.5}
        
        # Calculate number of questions per difficulty
        selected_questions = []
        
        # Add easy questions
        easy_count = int(num_questions * distribution["easy"])
        if easy_questions and easy_count > 0:
            selected_questions.extend(random.sample(easy_questions, min(easy_count, len(easy_questions))))
        
        # Add medium questions
        medium_count = int(num_questions * distribution["medium"])
        if medium_questions and medium_count > 0:
            selected_questions.extend(random.sample(medium_questions, min(medium_count, len(medium_questions))))
        
        # Add hard questions
        hard_count = num_questions - len(selected_questions)
        if hard_questions and hard_count > 0:
            selected_questions.extend(random.sample(hard_questions, min(hard_count, len(hard_questions))))
        
        # If we still need more questions, add from any remaining
        if len(selected_questions) < num_questions:
            remaining_questions = [q for q in questions if q not in selected_questions]
            additional_needed = num_questions - len(selected_questions)
            if remaining_questions:
                selected_questions.extend(random.sample(remaining_questions, min(additional_needed, len(remaining_questions))))
        
        return selected_questions
    
    def _generate_questions_for_subskill(self, skill_id: int, subskill_name: str, 
                                       difficulty: str, db: Session) -> List[Dict[str, Any]]:
        """Generate new questions for a subskill using AI"""
        try:
            # Generate questions using LLM
            questions = llm_integration.generate_quiz_questions(subskill_name, num_questions=3)
            
            # Save to database and format for quiz
            formatted_questions = []
            for question_data in questions:
                # Save to database
                quiz_question = QuizQuestion(
                    skill_id=skill_id,
                    subskill_name=subskill_name,
                    question=question_data.get('question'),
                    options=question_data.get('options', []),
                    correct_answer=question_data.get('correct_answer'),
                    explanation=question_data.get('explanation'),
                    difficulty=question_data.get('difficulty', difficulty),
                    created_by_ai=True
                )
                
                db.add(quiz_question)
                formatted_questions.append(self._format_question_data(question_data))
            
            db.commit()
            return formatted_questions
            
        except Exception as e:
            logger.error(f"Error generating questions for {subskill_name}: {str(e)}")
            return []
    
    def _format_question(self, question: QuizQuestion) -> Dict[str, Any]:
        """Format a QuizQuestion object for frontend consumption"""
        return {
            "id": question.id,
            "question": question.question,
            "options": question.options,
            "correct_answer": question.correct_answer,
            "explanation": question.explanation,
            "difficulty": question.difficulty,
            "subskill": question.subskill_name
        }
    
    def _format_question_data(self, question_data: Dict[str, Any]) -> Dict[str, Any]:
        """Format raw question data for frontend consumption"""
        return {
            "question": question_data.get('question'),
            "options": question_data.get('options', []),
            "correct_answer": question_data.get('correct_answer'),
            "explanation": question_data.get('explanation'),
            "difficulty": question_data.get('difficulty'),
            "subskill": question_data.get('subskill')
        }
    
    def _update_skill_progress_from_quiz(self, user_id: int, skill_id: int, score_percentage: float, db: Session):
        """Update user's skill progress based on quiz performance"""
        from models.models import SkillProgress
        
        # Get or create skill progress
        skill_progress = db.query(SkillProgress).filter(
            SkillProgress.user_id == user_id,
            SkillProgress.skill_id == skill_id
        ).first()
        
        if not skill_progress:
            skill_progress = SkillProgress(user_id=user_id, skill_id=skill_id)
            db.add(skill_progress)
        
        # Update average quiz score
        if skill_progress.average_quiz_score == 0:
            skill_progress.average_quiz_score = score_percentage
        else:
            # Moving average
            skill_progress.average_quiz_score = (skill_progress.average_quiz_score + score_percentage) / 2
        
        db.commit()
    
    def _calculate_quiz_xp(self, correct_answers: int, total_questions: int, time_taken: int) -> int:
        """Calculate XP based on quiz performance"""
        base_xp = correct_answers * 10  # 10 XP per correct answer
        
        # Bonus for perfect score
        if correct_answers == total_questions:
            base_xp += 20
        
        # Time bonus (if completed quickly)
        expected_time = total_questions * 120  # 2 minutes per question
        if time_taken < expected_time:
            time_bonus = int((expected_time - time_taken) / 30)  # 1 XP per 30 seconds saved
            base_xp += min(time_bonus, 10)  # Cap at 10 XP
        
        return base_xp
    
    def _award_xp(self, user_id: int, amount: int, transaction_type: str, skill_id: int, db: Session):
        """Award XP to user and update their total"""
        from models.models import XPTransaction, User
        
        # Create XP transaction
        xp_transaction = XPTransaction(
            user_id=user_id,
            amount=amount,
            transaction_type=transaction_type,
            description=f"Quiz completion reward",
            skill_id=skill_id
        )
        db.add(xp_transaction)
        
        # Update user's total XP
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.total_xp += amount
        
        db.commit()
    
    def _get_performance_level(self, score_percentage: float) -> str:
        """Get performance level description"""
        if score_percentage >= 90:
            return "Excellent"
        elif score_percentage >= 80:
            return "Very Good"
        elif score_percentage >= 70:
            return "Good"
        elif score_percentage >= 60:
            return "Fair"
        else:
            return "Needs Improvement"
    
    def _get_quiz_recommendations(self, score_percentage: float, feedback: List[Dict]) -> List[str]:
        """Generate recommendations based on quiz performance"""
        recommendations = []
        
        if score_percentage < 60:
            recommendations.append("Review the fundamentals before retaking the quiz")
            recommendations.append("Practice with additional resources")
        elif score_percentage < 80:
            recommendations.append("Focus on the topics you got wrong")
            recommendations.append("Try some intermediate-level practice exercises")
        else:
            recommendations.append("Great job! Consider moving to advanced topics")
            recommendations.append("Try teaching others to reinforce your knowledge")
        
        # Analyze specific weaknesses
        wrong_answers = [f for f in feedback if not f['is_correct']]
        if len(wrong_answers) > 0:
            recommendations.append(f"Pay special attention to: {', '.join([f['question'][:50] + '...' for f in wrong_answers[:2]])}")
        
        return recommendations
    
    def _fallback_quiz(self, skill_id: int, num_questions: int, db: Session) -> Dict[str, Any]:
        """Fallback quiz when AI generation fails"""
        skill = db.query(Skill).filter(Skill.id == skill_id).first()
        skill_name = skill.name if skill else "Unknown Skill"
        
        # Generate basic questions
        questions = []
        for i in range(min(num_questions, 3)):
            questions.append({
                "question": f"What is an important concept in {skill_name}?",
                "options": [
                    "Understanding the fundamentals",
                    "Memorizing everything",
                    "Skipping practice",
                    "Avoiding documentation"
                ],
                "correct_answer": "Understanding the fundamentals",
                "explanation": "Strong fundamentals are essential for mastering any skill.",
                "difficulty": "easy"
            })
        
        return {
            "skill_id": skill_id,
            "skill_name": skill_name,
            "questions": questions,
            "total_questions": len(questions),
            "estimated_time_minutes": len(questions) * 2,
            "difficulty_level": "beginner"
        }

# Global instance
quiz_manager = QuizManager()
