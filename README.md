# WortMeister

WortMeister is an advanced flashcard application designed specifically for German language learning, implementing the SuperMemo 2 (SM2) spaced repetition algorithm for optimal learning efficiency.

## Features

### Core Features
- **Advanced Spaced Repetition**: Implements the SM2 algorithm for optimal learning intervals
- **Bi-directional Learning**: Automatically creates reverse cards for comprehensive practice
- **Multiple Study Modes**:
  - **Study Mode**: Full spaced repetition with interval tracking
  - **Practice Mode**: Quick practice without affecting card intervals
- **Category Management**: Organize cards by categories
- **Search Functionality**: Quick search through all flashcards
- **Smart Text Processing**: 
  - Intelligent answer checking with normalization
  - Format preservation for complex grammar patterns
  - Line break handling for long phrases

### User Interface
- **Modern Kivy-based GUI**: Clean and responsive interface
- **Multiple Screens**:
  - Home Screen: Main navigation
  - Category Screen: Category selection
  - Study Screen: Interactive study interface
  - Add Card Screen: Card creation with category management
  - Search Screen: Card search functionality
- **Visual Feedback**: 
  - Color-coded responses
  - Animated transitions
  - Clear success/failure indicators

## Technical Architecture

### Project Structure
```
WortMeister/
├── core/
│   ├── algorithm/
│   │   ├── __init__.py
│   │   └── sm2.py          # SuperMemo 2 algorithm implementation
│   ├── utils/
│   │   ├── file_handler.py # Data persistence
│   │   ├── text_formatter.py
│   │   ├── text_processor.py
│   │   └── validation.py
│   ├── flashcard.py        # Flashcard model
│   └── manager.py          # Flashcard management
├── gui/
│   ├── kv/                 # Kivy UI definitions
│   │   ├── home_screen.kv
│   │   ├── category_screen.kv
│   │   ├── study_screen.kv
│   │   ├── add_card_screen.kv
│   │   └── search_screen.kv
│   ├── screens/
│   │   ├── study/         # Study mode implementations
│   │   │   ├── modes.py
│   │   │   ├── study_mode.py
│   │   │   └── practice_mode.py
│   │   ├── home_screen.py
│   │   ├── category_screen.py
│   │   ├── study_screen.py
│   │   └── add_card_screen.py
│   └── utils/             # GUI utilities
│       ├── ui_helpers.py
│       ├── ui_feedback.py
│       └── widget_styles.py
├── tests/                 # Comprehensive test suite
│   ├── core/             # Core functionality tests
│   └── gui/              # UI component tests
├── storage/              # Data storage
├── main.py              # Application entry point
└── app.kv               # Main Kivy configuration
```

### Core Components

#### SM2 Algorithm Implementation
- Adaptive interval calculation based on performance
- Quality rating system (0-5)
- Easiness factor adjustment
- Repetition count tracking

#### Flashcard Management
- CRUD operations for flashcards
- Category organization
- Bi-directional card creation
- Due card calculation

#### Data Processing
- Text normalization for answer checking
- Format preservation for complex answers
- Intelligent line break handling

### Testing

The project includes a comprehensive test suite covering:

- Core Algorithm Tests
  - SM2 algorithm calculations
  - Interval computations
  - Due date calculations
  
- Flashcard Tests
  - Answer validation
  - Review updates
  - Category management
  
- UI Component Tests
  - Screen interactions
  - Widget behavior
  - User input handling

Run tests using:
```bash
python tests/run_tests.py
```

## Development

### Requirements
- Python 3.8+
- Kivy 2.2.1+
- Additional dependencies in requirements.txt

### Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python main.py`

### Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Submit a pull request

## License
This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback:
- Email: [s.dvid@hotmail.com](mailto:s.dvid@hotmail.com)
- GitHub: [DvidMakesThings](https://github.com/DvidMakesThings)