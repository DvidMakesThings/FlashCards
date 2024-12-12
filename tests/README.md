# Test Documentation

## Overview
This directory contains the comprehensive test suite for the WortMeister application. The tests are organized into core and GUI components, with detailed specifications and pass/fail criteria for each test case.

## Test Structure

```
tests/
├── core/                          # Core functionality tests
│   ├── test_flashcard.py          # Flashcard model tests
│   ├── test_manager.py            # FlashcardManager tests
│   ├── test_sm2.py                # SM2 algorithm tests
│   └── test_text_processor.py     # Text processing tests
├── gui/                           # GUI component tests
│   ├── test_study_controller.py   # Study controller tests
│   ├── test_study_modes.py        # Study modes tests
│   ├── test_study_screen.py       # Study screen tests
│   └── test_ui_helpers.py         # UI utility tests
├── html_test_runner.py            # Custom HTML report generator
├── conftest.py                    # Test configuration
└── run_tests.py                   # Test runner script
```

## Test Categories

### Core Tests

#### Flashcard Tests (`test_flashcard.py`)
- **Answer Validation**
  - Exact match testing
  - Case-insensitive comparison
  - Whitespace handling
  - Line break normalization
- **Review Updates**
  - Interval calculations
  - Easiness factor adjustments
  - Review date tracking

#### Manager Tests (`test_manager.py`)
- **Card Management**
  - Adding new cards
  - Retrieving due cards
  - Category filtering
  - Duplicate prevention
- **Data Persistence**
  - Save/load operations
  - File handling
  - Data integrity

#### SM2 Algorithm Tests (`test_sm2.py`)
- **Interval Calculations**
  - Perfect recall handling
  - Poor performance adjustments
  - Review scheduling
- **Quality Conversion**
  - Difficulty rating mapping
  - Boundary conditions
- **Due Date Logic**
  - Past/future review dates
  - Initial card handling

#### Text Processing Tests (`test_text_processor.py`)
- **Text Normalization**
  - Space handling
  - Line break processing
  - Accent removal
- **Format Preservation**
  - Grammar structure
  - Special characters
  - Line breaks

### GUI Tests

#### Study Controller Tests (`test_study_controller.py`)
- **Card Loading**
  - Empty category handling
  - Card sequence management
- **Mode Switching**
  - Study/Practice transitions
  - State preservation

#### Study Modes Tests (`test_study_modes.py`)
- **Practice Mode**
  - Answer checking
  - Feedback display
  - Next card handling
- **Study Mode**
  - Interval updates
  - Difficulty rating
  - Progress tracking

#### Study Screen Tests (`test_study_screen.py`)
- **User Interface**
  - Input handling
  - Feedback display
  - Button states
- **Answer Processing**
  - Format handling
  - Feedback accuracy
  - State transitions

#### UI Helper Tests (`test_ui_helpers.py`)
- **Visual Feedback**
  - Color schemes
  - Text formatting
- **Widget Management**
  - Visibility toggling
  - State synchronization

## Test Execution

### Running Tests
```bash
python tests/run_tests.py
```

### Test Report
The test runner generates a detailed HTML report including:
- Test execution summary
- Individual test results
- Pass/fail status
- Error details
- Test specifications
- Pass/fail criteria

### Configuration
Test environment configuration in `conftest.py`:
- Temporary storage setup
- Kivy test configuration
- Fixture definitions

## Writing Tests

### Test Structure
Each test should include:
```python
def test_something(self):
    """Test description.
    
    Specification:
        Detailed test specification
        
    Criteria:
        - Specific pass/fail criteria
        - Expected behaviors
        - Edge cases
    """
    # Test implementation
```

### Best Practices
1. **Isolation**: Each test should be independent
2. **Clear Purpose**: One assertion per test
3. **Documentation**: Include specifications and criteria
4. **Setup/Teardown**: Use fixtures for common setup
5. **Error Handling**: Test both success and failure cases

## Coverage

The test suite aims for comprehensive coverage of:
- Core functionality
- User interface components
- Edge cases
- Error conditions
- Integration points

## Dependencies
- pytest
- pytest-kivy
- pytest-cov
- coverage
- jinja2 (for report generation)