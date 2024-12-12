from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from core.manager import FlashcardManager
from core.utils.validation import validate_card_input
from gui.utils.ui_helpers import get_feedback_color

class AddCardScreen(Screen):
    flashcard_manager = ObjectProperty(None)  # Use Kivy property for proper initialization

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flashcard_manager = FlashcardManager()

    def on_enter(self):
        """Called when screen is entered."""
        self.ids.category_spinner.values = self.get_categories() + ["Add New Category"]

    def get_categories(self):
        """Retrieve a sorted list of unique categories."""
        categories = {getattr(card, 'category', 'Uncategorized') 
                     for card in self.flashcard_manager.cards}
        return sorted(categories) if categories else ["Default"]

    def toggle_custom_category(self, selected_text):
        """Show or hide the custom category input field based on spinner selection."""
        custom_box = self.ids.custom_category_box
        if selected_text == "Add New Category":
            custom_box.height = '48dp'
            custom_box.opacity = 1
        else:
            custom_box.height = 0
            custom_box.opacity = 0

    def save_card(self):
        """Save a new card after validation."""
        category = (
            self.ids.custom_category_input.text.strip()
            if self.ids.custom_category_box.height > 0
            else self.ids.category_spinner.text.strip()
        )
        question = self.ids.question_input.text.strip()
        answer = self.ids.answer_input.text.strip()

        # Validate inputs
        is_valid, error_message = validate_card_input(category, question, answer)
        if not is_valid:
            self.display_feedback(error_message, get_feedback_color(False))
            return

        # Add the card
        result = self.flashcard_manager.add_card(question, answer, category)
        if not result:
            self.display_feedback("Card already exists!", get_feedback_color(False))
            return

        # Update available categories
        self.ids.category_spinner.values = self.get_categories() + ["Add New Category"]

        # Success feedback
        self.display_feedback("Card added successfully!", get_feedback_color(True))

        # Reset inputs
        self.reset_inputs()

    def display_feedback(self, message, color):
        """Display feedback to the user through the GUI."""
        self.ids.feedback_label.text = message
        self.ids.feedback_label.color = color

    def reset_inputs(self):
        """Reset input fields and hide the custom category box if visible."""
        self.ids.question_input.text = ""
        self.ids.answer_input.text = ""
        if self.ids.custom_category_box.height > 0:
            self.ids.custom_category_input.text = ""
            self.ids.custom_category_box.height = 0
            self.ids.custom_category_box.opacity = 0