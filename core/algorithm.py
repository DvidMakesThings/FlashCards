"""
Spaced repetition algorithm implementation.
"""
from datetime import datetime, timedelta

def calculate_next_review(score: str, current_interval: int) -> int:
    """Calculate the next review interval based on performance."""
    if score == 'easy':
        return current_interval * 2
    elif score == 'hard':
        return max(1, current_interval // 2)
    return current_interval

def is_due(last_review: str, interval: int) -> bool:
    """Check if a card is due for review."""
    if not last_review:
        return True
        
    last_date = datetime.strptime(last_review, '%Y-%m-%d')
    next_review_date = last_date + timedelta(days=interval)
    return next_review_date <= datetime.now()