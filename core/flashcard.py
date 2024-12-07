# File: core/flashcard.py
from datetime import datetime

class Flashcard:
    def __init__(self, question, answer, interval, last_review, score, category):
        self.question = question
        self.answer = answer
        self.interval = interval
        self.last_review = last_review
        self.score = score
        self.category = category

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer.strip().lower()

    def update_review(self, difficulty):
        from core.algorithm import calculate_next_review
        self.interval = calculate_next_review(difficulty, self.interval)
        self.last_review = datetime.now().strftime('%Y-%m-%d')