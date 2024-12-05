# File: core/algorithm.py
from datetime import datetime, timedelta

def calculate_next_review(score, current_interval):
    if score == 'easy':
        next_interval = current_interval * 2
    elif score == 'hard':
        next_interval = max(1, current_interval // 2)
    else:
        next_interval = current_interval
    return next_interval

def is_due(last_review, interval):
    last_date = datetime.strptime(last_review, '%Y-%m-%d')
    next_review_date = last_date + timedelta(days=interval)
    return next_review_date <= datetime.now()