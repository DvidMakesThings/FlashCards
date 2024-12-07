from datetime import datetime

class Flashcard:
    """
    The Flashcard class represents a single flashcard object with a question, answer, 
    review interval, last review date, score, and category.
    
    This class provides functionality to check the user's answer and update the review 
    details based on the difficulty of the user's response.
    """

    def __init__(self, question, answer, interval, last_review, score, category):
        """
        Initializes the Flashcard object with the provided question, answer, interval, 
        last review date, score, and category.
        
        Parameters:
            question (str): The question text for the flashcard.
            answer (str): The answer to the question.
            interval (int): The review interval (in days) for the flashcard.
            last_review (str): The date when the card was last reviewed (in 'YYYY-MM-DD' format).
            score (int): The score representing the user's success with the card.
            category (str): The category to which the flashcard belongs.
        """
        self.question = question
        self.answer = answer
        self.interval = interval
        self.last_review = last_review
        self.score = score
        self.category = category

    def check_answer(self, user_answer):
        """
        Checks whether the user's answer is correct, case-insensitively and ignoring extra spaces.
        
        Parameters:
            user_answer (str): The answer provided by the user.
        
        Returns:
            bool: True if the user's answer matches the correct answer, otherwise False.
        """
        # Normalize and compare the user's answer with the correct answer
        return user_answer.strip().lower() == self.answer.strip().lower()

    def update_review(self, difficulty):
        """
        Updates the review interval and last review date for the flashcard based on the 
        user's difficulty level for the answer.
        
        The difficulty affects the review interval (how soon the card should be reviewed again).
        
        Parameters:
            difficulty (str): The difficulty level of the user's answer ("easy", "medium", "hard").
        """
        # Import the function that calculates the next review interval based on difficulty
        from core.algorithm import calculate_next_review
        
        # Update the interval and last review date based on the difficulty
        self.interval = calculate_next_review(difficulty, self.interval)
        self.last_review = datetime.now().strftime('%Y-%m-%d')  # Set last review to the current date
