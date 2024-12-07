from datetime import datetime, timedelta

def calculate_next_review(score, current_interval):
    """
    Calculates the next review interval for a flashcard based on the user's performance 
    and the current interval.

    This function adjusts the review interval based on the difficulty of the user's answer 
    to a flashcard. The interval increases if the user finds the answer easy and decreases 
    if the user finds it hard.

    Parameters:
        score (str): The user's performance on the flashcard, which could be one of 'easy', 'hard', or 'normal'.
        current_interval (int): The current review interval in days.

    Returns:
        int: The updated review interval for the flashcard, based on the user's performance.
    """
    if score == 'easy':
        # If the user found the answer easy, double the review interval
        next_interval = current_interval * 2
    elif score == 'hard':
        # If the user found the answer hard, reduce the review interval (but not below 1)
        next_interval = max(1, current_interval // 2)
    else:
        # If the user gave a normal answer, keep the interval the same
        next_interval = current_interval

    return next_interval


def is_due(last_review, interval):
    """
    Determines whether a flashcard is due for review based on the last review date and 
    the current review interval.

    This function calculates the next review date by adding the current interval to the 
    last review date. If the calculated next review date is today or earlier, the flashcard 
    is due for review.

    Parameters:
        last_review (str): The date the flashcard was last reviewed, in the format 'YYYY-MM-DD'.
        interval (int): The current review interval in days.

    Returns:
        bool: True if the flashcard is due for review, otherwise False.
    """
    # Convert the 'last_review' string to a datetime object
    last_date = datetime.strptime(last_review, '%Y-%m-%d')

    # Calculate the next review date by adding the interval to the last review date
    next_review_date = last_date + timedelta(days=interval)

    # Compare the next review date with the current date
    return next_review_date <= datetime.now()
