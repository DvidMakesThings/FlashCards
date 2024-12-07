# File: screens.py
import json
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from core.manager import FlashcardManager
from kivy.clock import Clock
import unicodedata


class CategoryScreen(Screen):
    def on_pre_enter(self):
        self.update_category_list()

    def update_category_list(self):
        self.ids.category_list.clear_widgets()  # Clear existing buttons
        categories = self.get_available_categories()
        for category in categories:
            print(f"[DEBUG] Adding button for category: {category}")
            btn = Button(
                text=category,
                size_hint_y=None,
                height='40dp',
                background_color=(0.2, 0.6, 0.9, 1),  # Soft blue background
                color=(1, 1, 1, 1),  # White text for contrast
                font_size='18sp'
            )
            btn.bind(on_press=self.select_category)  # Bind the button to the select_category method
            self.ids.category_list.add_widget(btn)


    def get_available_categories(self):
        import os
        categories = set()
        for file in os.listdir('storage'):
            if file.endswith('.json'):
                with open(os.path.join('storage', file), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for card in data:
                        if 'category' in card:
                            categories.add(card['category'])
        print(f"[DEBUG] Categories found: {categories}")
        return sorted(categories)

    def select_category(self, button):
        category = button.text
        print(f"[DEBUG] Selected category: {category}")
        study_screen = self.manager.get_screen('study')
        study_screen.set_category(category)
        self.manager.current = 'study'


class HomeScreen(Screen):
    pass


class StudyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flashcard_manager = None
        self.current_card = None
        self.practice_mode = False  # Initialize this attribute to avoid AttributeError

    def set_category(self, category):
        print(f"[DEBUG] Setting category for StudyScreen: {category}")
        self.category = category  # Store the selected category

        # Initialize the flashcard manager with the selected category
        self.flashcard_manager = FlashcardManager(category=self.category)

        # Now load the next card with the selected category
        self.load_next_card()

    def start_practice_mode(self):
        if not self.flashcard_manager or not self.flashcard_manager.cards:
            print("[ERROR] No cards to review!")
            self.ids.question_label.text = "No cards available!"
            return
        print(f"[DEBUG] Starting practice mode with {len(self.flashcard_manager.cards)} cards.")
        self.practice_mode = True
        self.load_next_card()

    def load_next_card(self):
        if not self.category:
            print("[ERROR] No category selected!")
            return

        # Get the next card (don't write to the file)
        due_cards = self.flashcard_manager.get_due_cards(self.category)

        if due_cards:
            self.current_card = due_cards[0]  # Get the next due card
            print(f"[DEBUG] Loaded due card: {self.current_card.question}")  # Show the question instead of the object
            
            # Display the question on the UI
            self.ids.question_label.text = self.current_card.question
            # Do NOT display the answer here! Just allow the user to input their answer

        else:
            print(f"[DEBUG] No due cards found for category: {self.category}")
            self.ids.question_label.text = "No due cards for this category."

    def normalize_text(self, text):
        return unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8').lower()

    def check_user_answer(self):
        if not self.current_card:
            return

        # Normalize the text for case-insensitive comparison
        user_answer = self.normalize_text(self.ids.user_input.text)
        correct_answer = self.normalize_text(self.current_card.answer)
        
        # If the answer is correct
        if user_answer == correct_answer:
            # Provide positive feedback and display green message
            self.ids.feedback_label.text = "Correct!"  
            self.ids.feedback_label.color = 0, 0.5, 0, 1  # Green color for correct answer

            # If not in practice mode, update review score (but don't save data)
            if not self.practice_mode:
                self.current_card.update_review("easy")
            
            # Wait for 0.5 seconds before showing the next card
            Clock.schedule_once(lambda dt: self.next_question(), 0.5)
            
        else:
            # If the answer is incorrect
            self.ids.feedback_label.text = f"Incorrect!\nCorrect answer: {self.current_card.answer}"  # Display correct answer under "Incorrect"
            self.ids.feedback_label.color = 1, 0, 0, 1  # Red color for incorrect answer

            # Show the "Next" button
            self.show_next_button()

            # Update review score as hard if the answer was incorrect (but don't save data)
            if not self.practice_mode:
                self.current_card.update_review("hard")
        
        # Do NOT clear the input field here when the answer is wrong (keep the wrong answer visible)
        # Clear the input field after clicking the "Next" button



    def show_next_button(self):
        # Show the "Next" button so the user can proceed manually
        self.ids.next_button.opacity = 1
        self.ids.next_button.size_hint_y = None
        self.ids.next_button.height = '60dp'

    def hide_next_button(self):
        # Hide the "Next" button
        self.ids.next_button.opacity = 0
        self.ids.next_button.size_hint_y = None
        self.ids.next_button.height = '0dp'


    def next_question(self):
        if self.practice_mode:
            # Move current card to end for endless mode
            self.flashcard_manager.cards.append(self.flashcard_manager.cards.pop(0))
            self.load_all_cards()
        else:
            # Load the next card and reset feedback
            self.load_next_card()
            self.hide_next_button()  # Hide the "Next" button after answering
            
            # Clear the feedback label and reset color
            self.ids.feedback_label.text = ""  # Clear feedback text
            self.ids.feedback_label.color = 1, 1, 1, 1  # Reset color to default
        
        # Clear the user input field after moving to the next question
        self.ids.user_input.text = ""  # Clear the input field when moving to the next card

class AddCardScreen(Screen):
    flashcard_manager = None  # Class-level attribute

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        """Initialize flashcard_manager after KV is fully loaded."""
        self.flashcard_manager = FlashcardManager()
        # Refresh spinner values
        self.ids.category_spinner.values = self.get_categories() + ["Add New Category"]

    def get_categories(self):
        """Retrieve a sorted list of unique categories."""
        if not self.flashcard_manager:
            return ["Loading..."]
        categories = {getattr(card, 'category', 'Uncategorized') for card in self.flashcard_manager.cards}
        print(f"[DEBUG] Existing categories: {categories}")
        return sorted(categories)


    def toggle_custom_category(self, selected_text):
        """Show or hide the custom category input field based on spinner selection."""
        if selected_text == "Add New Category":
            self.ids.custom_category_box.opacity = 1
            self.ids.custom_category_box.height = 120  # Ensure the box height is set correctly
        else:
            self.ids.custom_category_box.opacity = 0
            self.ids.custom_category_box.height = 0  # Hide the box by reducing height to 0

    def save_card(self):
        """Save a new card after validation."""
        category = (
            self.ids.custom_category_input.text.strip()
            if self.ids.custom_category_box.height > 0
            else self.ids.category_spinner.text.strip()
        )
        question = self.ids.question_input.text.strip()
        answer = self.ids.answer_input.text.strip()

        # Validation
        if not category or category == "Select or Add Category":
            self.display_feedback("Please select or add a category.", (1, 0, 0, 1))  # Red for error
            return
        if not question:
            self.display_feedback("Question field cannot be empty.", (1, 0, 0, 1))
            return
        if not answer:
            self.display_feedback("Answer field cannot be empty.", (1, 0, 0, 1))
            return

        # Add the card
        result = self.flashcard_manager.add_card(question, answer, category)
        if not result:
            self.display_feedback("Card already exists!", (1, 0, 0, 1))  # Orange for warning
            return

        # Update available categories
        self.ids.category_spinner.values = self.get_categories() + ["Add New Category"]

        # Success feedback
        self.display_feedback("Card added successfully!", (0, 0.5, 0, 1))  # Green for success

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
