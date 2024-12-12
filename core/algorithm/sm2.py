"""
SuperMemo 2 (SM2) algorithm implementation.

The SM2 algorithm is used for spaced repetition learning, calculating optimal intervals
between reviews based on the learner's performance.
"""
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Tuple

@dataclass
class SM2Data:
    """Data structure for SM2 algorithm parameters."""
    easiness: float = 2.5  # Initial easiness factor
    interval: int = 1      # Current interval in days
    repetitions: int = 0   # Number of successful repetitions

def calculate_next_review(
    quality: int,
    current_data: SM2Data
) -> Tuple[SM2Data, datetime]:
    """
    Calculate the next review date using the SM2 algorithm.
    
    Args:
        quality: Rating of recall quality (0-5)
            0 = Complete blackout
            1 = Incorrect, but remembered upon seeing answer
            2 = Incorrect, but answer looked familiar
            3 = Correct with difficulty
            4 = Correct with some hesitation
            5 = Perfect recall
        current_data: Current SM2 algorithm data
        
    Returns:
        Tuple containing:
            - Updated SM2Data
            - Next review datetime
    """
    if quality < 0:
        quality = 0
    if quality > 5:
        quality = 5

    # Update easiness factor
    easiness = current_data.easiness + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    
    # Maintain minimum easiness factor
    if easiness < 1.3:
        easiness = 1.3

    # Reset or increment repetitions based on quality
    if quality < 3:
        repetitions = 0
        interval = 1
    else:
        repetitions = current_data.repetitions + 1
        if repetitions == 1:
            interval = 1
        elif repetitions == 2:
            interval = 6
        else:
            interval = round(current_data.interval * easiness)

    # Calculate next review date
    next_review = datetime.now() + timedelta(days=interval)

    return SM2Data(
        easiness=easiness,
        interval=interval,
        repetitions=repetitions
    ), next_review

def quality_from_difficulty(difficulty: str) -> int:
    """
    Convert difficulty rating to SM2 quality score.
    
    Args:
        difficulty: User-friendly difficulty rating
        
    Returns:
        int: SM2 quality score (0-5)
    """
    quality_map = {
        'again': 0,      # Complete blackout
        'hard': 2,       # Answer looked familiar
        'good': 3,       # Correct with difficulty
        'easy': 5        # Perfect recall
    }
    return quality_map.get(difficulty, 3)  # Default to 'good' if unknown

def is_due(last_review: str | None, interval: int) -> bool:
    """
    Check if a card is due for review.
    
    Args:
        last_review: Date of last review (YYYY-MM-DD format)
        interval: Current interval in days
        
    Returns:
        bool: True if card is due for review
    """
    if not last_review:
        return True
        
    last_date = datetime.strptime(last_review, '%Y-%m-%d')
    next_review = last_date + timedelta(days=interval)
    return datetime.now() >= next_review