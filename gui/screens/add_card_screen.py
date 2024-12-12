from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from core.manager import FlashcardManager
from core.utils.validation import validate_card_input
from gui.utils.ui_helpers import get_feedback_color

class AddCardScreen(Screen):
    flashcard_manager = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flashcard_manager = FlashcardManager()

    def on_kv_post(self, base_widget):
        """Called after kv file is loaded."""
        super().on_kv_post(base_widget)
        # Initialize custom category input state
        self.ids.custom_category_input.disabled = True
        self.ids.custom_category_input.text = ""

    def on_enter(self):
        """Called when screen is entered."""
        # Update spinner values
        self.ids.category_spinner.values = self.get_categories() + ["Add New Category"]
        # Reset category input state
        self.ids.custom_category_input.disabled = True
        self.ids.custom_category_input.text = ""
        # Reset spinner selection
        self.ids.category_spinner.text = "Select or Add Category"

    def get_categories(self):
        """Retrieve a sorted list of unique categories."""
        categories = {getattr(card, 'category', 'Uncategorized') 
                     for card in self.flashcard_manager.cards}
        return sorted(categories) if categories else ["Default"]

    def toggle_custom_category(self, selected_text):
        """Enable/disable the custom category input based on selection."""
        is_add_new = selected_text == "Add New Category"
        self.ids.custom_category_input.disabled = not is_add_new
        if not is_add_new:
            self.ids.custom_category_input.text = ""

    def save_card(self):
        """Save a new card after validation."""
        category = (
            self.ids.custom_category_input.text.strip()
            if self.ids.category_spinner.text == "Add New Category"
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
        """Reset input fields."""
        self.ids.question_input.text = ""
        self.ids.answer_input.text = ""
        self.ids.custom_category_input.text = ""
        self.ids.category_spinner.text = "Select or Add Category"
        self.ids.custom_category_input.disabled = True