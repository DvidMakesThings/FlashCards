# FlashCards

Flashcards app for German learning

The best algorithm for a flashcard app in language learning is the spaced repetition algorithm (e.g., the SM2 algorithm from the SuperMemo method). Here's how it works:

- **Initial Review**: When a new card is introduced, the user reviews it shortly after learning.
- **Intervals**: Cards the user answers correctly are shown less frequently, while those answered incorrectly appear more often.
- **Scoring**: Each card is scored based on the user’s response (e.g., "easy," "hard"). This score adjusts the interval until the card is shown again.
- **Adaptive Learning**: Cards with higher error rates are prioritized, reinforcing weaker areas.

Spaced repetition is effective because it optimizes recall by showing cards just before they're likely to be forgotten, maximizing long-term retention.

## High-Level Design

### Data Storage

Store flashcards in a JSON or SQLite database. Each card has:

- Question
- Answer
- Review Interval
- Last Reviewed Date
- Score

### Core Components

- **Card Management**: Add, edit, or delete cards.
- **Review Algorithm**: Implement spaced repetition logic (e.g., SM2 algorithm).
- **Study Session**: Show cards due for review, handle user input, and update review intervals.
- **User Interface**: CLI (initially) or GUI using frameworks like Tkinter, PyQt, or Kivy.

### Project Structure

```
flashcards_app/
├── main.py             # Entry point for the program
├── app.kv              # Kivy layout file (UI design)
├── core/
│   ├── flashcard.py    # Flashcard class and data model
│   ├── manager.py      # Flashcard manager (CRUD operations)
│   └── algorithm.py    # Spaced repetition algorithm
├── gui/
│   ├── screens.py      # Screen management (Study, Add Card, etc.)
│   ├── widgets.py      # Custom widgets (e.g., buttons, labels)
│   └── handlers.py     # Event and user interaction handlers
├── storage/
│   └── data.json       # Stores flashcard data (or SQLite DB)
└── unittest/
    └── reports           # Stores report files
```

### High-Level Design Overview

#### Core Modules

- **flashcard.py**: Defines the structure of a flashcard and includes methods to check answers and update review intervals.
- **manager.py**: Handles the management of flashcards (CRUD operations) and interacts with the storage layer to load/save flashcards.
- **algorithm.py**: Implements the spaced repetition algorithm to calculate review intervals.

#### GUI Modules

- **screens.py**: Manages individual screens for the app (Home, Study, Add Flashcard) and connects them to logic via event handlers.
- **widgets.py**: Contains reusable custom widgets for the GUI, such as buttons, labels, or input fields.
- **handlers.py**: Handles user interactions, e.g., checking answers, switching screens, and saving updates to the manager.

### Storage

- **data.json**: Stores the flashcard data persistently (or optionally SQLite).

### Main Program

- **main.py**: Initializes the app, sets up the screen manager, and launches the GUI.

### Interaction Diagram

```
       +---------------------------+
       |        main.py            |
       |  Initializes App and GUI  |
       +---------------------------+
                  ↓
       +---------------------------+
       |         screens.py         |
       | Manages App Screens (Home, |
       | Study, Add Card) and Links |
       |         to Logic           |
       +---------------------------+
                  ↓
       +---------------------------+
       |        handlers.py         |
       | Handles Events:            |
       | - User Answer Check        |
       | - Screen Navigation        |
       +---------------------------+
                  ↓
       +---------------------------+
       |        manager.py          |
       | Loads, Saves, and Updates  |
       | Flashcards from Storage    |
       +---------------------------+
                  ↓
       +---------------------------+
       |       flashcard.py         |
       | Flashcard Class:           |
       | - Data Structure           |
       | - Review/Check Logic       |
       +---------------------------+
                  ↓
       +---------------------------+
       |       algorithm.py         |
       | Calculates New Review      |
       | Intervals (Spaced Repetition)|
       +---------------------------+
                  ↓
       +---------------------------+
       |        data.json           |
       | Persistent Storage of      |
       | Flashcards                 |
       +---------------------------+
```

### Flow Example: User Checks an Answer

**User Interaction**:
- User opens the "Study" screen, sees a question, and types an answer.

**Answer Validation**:
- The StudyScreen in `screens.py` triggers a method in `handlers.py` to check the user's answer.

**Flashcard Logic**:
- `handlers.py` calls the `check_answer` method in `flashcard.py` to validate the user's input. The result determines whether the feedback is "Correct!" or "Incorrect!"

**Review Update**:
- If the answer is correct, the interval is updated using logic in `algorithm.py`. The FlashcardManager saves the updated flashcard data to `data.json`.

**Storage**:
- The updated data is saved back to `data.json` for persistence.

### Advantages of This Design

- **Modularity**: Core logic (e.g., spaced repetition) is separate from GUI components, making it reusable and easier to debug.
- **Extensibility**: You can replace `data.json` with SQLite or add new screens without affecting existing components.
- **Separation of Concerns**: Each module has a clear responsibility:
  - Core handles the logic and data.
  - GUI focuses on user interaction.
  - Handlers bridge the gap between the two.