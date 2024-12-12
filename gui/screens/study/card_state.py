"""
Card state management.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class CardState:
    """Represents the current state of a flashcard in study."""
    answer_shown: bool = False
    last_attempt: Optional[str] = None
    correct_count: int = 0
    incorrect_count: int = 0
    
    def record_attempt(self, correct: bool) -> None:
        """Record an answer attempt."""
        self.last_attempt = datetime.now().isoformat()
        if correct:
            self.correct_count += 1
        else:
            self.incorrect_count += 1