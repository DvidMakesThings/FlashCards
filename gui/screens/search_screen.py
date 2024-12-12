"""
Search screen implementation.
"""
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from core.manager import FlashcardManager
from functools import partial

class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flashcard_manager = FlashcardManager()
        
    def on_text_change(self, instance, value):
        """Handle search text changes with debouncing."""
        Clock.unschedule(self._do_search)
        Clock.schedule_once(partial(self._do_search, value), 0.5)
        
    def _do_search(self, search_text, *args):
        """Perform search in questions and update results."""
        self.ids.results_grid.clear_widgets()
        if not search_text:
            return
            
        search_text = search_text.lower()
        matching_cards = [
            card for card in self.flashcard_manager.cards
            if search_text in card.question.lower()
        ]
        
        for card in matching_cards:
            self.add_result_card(card)
            
    def add_result_card(self, card):
        """Add a card-style result to the grid."""
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        
        # Create card container
        card_box = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height='120dp',
            padding='10dp',
            spacing='5dp'
        )
        
        # Add white background with rounded corners
        with card_box.canvas.before:
            from kivy.graphics import Color, RoundedRectangle
            Color(1, 1, 1, 0.9)
            RoundedRectangle(pos=card_box.pos, size=card_box.size, radius=[15])
        
        # Question label
        question_label = Label(
            text=f"{card.question}",
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height='40dp',
            halign='left',
            valign='middle'
        )
        question_label.bind(width=lambda *x: setattr(question_label, 'text_size', (question_label.width, None)))
        
        # Answer label
        answer_label = Label(
            text=f"{card.answer}",
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height='40dp',
            halign='left',
            valign='middle'
        )
        answer_label.bind(width=lambda *x: setattr(answer_label, 'text_size', (answer_label.width, None)))
        
        card_box.bind(size=self._update_card_background)
        card_box.add_widget(question_label)
        card_box.add_widget(answer_label)
        
        self.ids.results_grid.add_widget(card_box)
        
    def _update_card_background(self, instance, value):
        """Update card background when size/position changes."""
        instance.canvas.before.clear()
        with instance.canvas.before:
            from kivy.graphics import Color, RoundedRectangle
            Color(1, 1, 1, 0.9)
            RoundedRectangle(pos=instance.pos, size=instance.size, radius=[15])