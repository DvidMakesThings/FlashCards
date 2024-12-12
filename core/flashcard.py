"""
Core flashcard model implementation.
"""
from datetime import datetime
from dataclasses import dataclass
from core.utils.text_processing import normalize_text, compare_answers
from core.algorithm.sm2 import SM2Data, calculate_next_review, quality_from_difficulty

@dataclass
class Flashcard:
    """Represents a single flashcard with question, answer, and review data."""
    
    question: str
    answer: str
    category: str
    interval: int = 1
    last_review: str | None = None
    repetitions: int = 0
    easiness: float = 2.5
    score: int = 0

    def check_answer(self, user_answer: str) -> bool:
        """Check if the user's answer matches the correct answer."""
        return compare_answers(user_answer, self.answer)

    def update_review(self, difficulty: str) -> None:
        """
        Update review data based on answer difficulty.
        
        Args:
            difficulty: User-rated difficulty ('again', 'hard', 'good', 'easy')
        """
        # Convert current state to SM2Data
        current_data = SM2Data(
            easiness=self.easiness,
            interval=self.interval,
            repetitions=self.repetitions
        )
        
        # Calculate next review using SM2 algorithm
        quality = quality_from_difficulty(difficulty)
        new_data, next_review = calculate_next_review(quality, current_data)
        
        # Update card with new values
        self.easiness = new_data.easiness
        self.interval = new_data.interval
        self.repetitions = new_data.repetitions
        self.last_review = datetime.now().strftime('%Y-%m-%d')
        
        # Update score based on quality
        if quality >= 4:
            self.score += 1
        elif quality <= 2:
            self.score = max(0, self.score - 1)