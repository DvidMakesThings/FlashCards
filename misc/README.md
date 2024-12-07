# Flashcards Generator for Vocabulary

This script generates flashcards from a vocabulary file and formats them into a JSON structure suitable for a spaced repetition flashcard application.

## Overview

The script allows you to convert a vocabulary file, containing word pairs (German and Hungarian), into **flashcards**. Each word pair is used to generate two flashcards:

1. **German -> Hungarian**
2. **Hungarian -> German**

The flashcards are then saved in a JSON file with the following structure:

```json
[
    {
        "question": "word_in_german",
        "answer": "word_in_hungarian",
        "interval": 2,
        "last_review": null,
        "score": 0,
        "category": "category_name"
    },
    {
        "question": "word_in_hungarian",
        "answer": "word_in_german",
        "interval": 2,
        "last_review": null,
        "score": 0,
        "category": "category_name"
    }
]
```

## Features

- **Generate Flashcards**: Automatically generate flashcards from a vocabulary file.
- **Two Directions**: For each word pair, two flashcards are created: one for the German-to-Hungarian translation and one for the Hungarian-to-German translation.
- **Custom Categories**: You can specify a custom category for the flashcards.
- **JSON Format**: The flashcards are saved in a JSON file that can be imported into flashcard apps or other spaced repetition systems.

## Requirements

- **Python 3.x**: This script is written in Python 3.
- **Command-Line Interface**: The script uses `argparse` to handle input arguments from the command line.

## Installation

Ensure that you have Python 3 installed on your system. No external libraries or dependencies are required for this script.

## Usage

### Command-Line Arguments

To run the script, use the following syntax:

```bash
python generate_flashcards.py --file <path_to_vocab_file> --category <category_name>
```

**Arguments**:
- `--file`: (Required) The path to the vocabulary file containing the word pairs (e.g., `vocab.txt`).
- `--category`: (Required) The category under which the flashcards will be grouped (e.g., `German_Hungarian`).

### Example Command

Prepare the Vocabulary File:
Ensure your vocabulary file (`vocab.txt`) follows this format:

```text
der Hund - kutya
die Katze - macska
der Apfel - alma
```

Run the Script:

```bash
python generate_flashcards.py --file vocab.txt --category German_Hungarian
```

This command will generate flashcards for the words in `vocab.txt` and save them in a file named `German_Hungarian.json`.

## Input File Format

The vocabulary file should contain word pairs in the following format:

```text
german_word - hungarian_word
```

Where:
- `german_word`: The German word (or phrase).
- `hungarian_word`: The corresponding Hungarian translation (or phrase).

Lines that do not contain ' - ' (such as empty lines or improperly formatted lines) will be ignored.

## Output

After running the script, the flashcards will be generated and saved in a `.json` file named according to the specified category.

For example, if you use the category `German_Hungarian`, the output file will be:

```text
German_Hungarian.json
```

The file will contain a JSON array with each flashcard in the following structure:

```json
[
    {
        "question": "der Hund",
        "answer": "kutya",
        "interval": 2,
        "last_review": null,
        "score": 0,
        "category": "German_Hungarian"
    },
    {
        "question": "kutya",
        "answer": "der Hund",
        "interval": 2,
        "last_review": null,
        "score": 0,
        "category": "German_Hungarian"
    },
    {
        "question": "die Katze",
        "answer": "macska",
        "interval": 2,
        "last_review": null,
        "score": 0,
        "category": "German_Hungarian"
    },
    {
        "question": "macska",
        "answer": "die Katze",
        "interval": 2,
        "last_review": null,
        "score": 0,
        "category": "German_Hungarian"
    },
    {
        "question": "der Apfel",
        "answer": "alma",
        "interval": 2,
        "last_review": null,
        "score": 0,
        "category": "German_Hungarian"
    },
    {
        "question": "alma",
        "answer": "der Apfel",
        "interval": 2,
        "last_review": null,
        "score": 0,
        "category": "German_Hungarian"
    }
]
```

## Script Behavior

- **Word Pairs**: Each word pair from the vocabulary file generates two flashcards — one for each direction (German to Hungarian and vice versa).
- **Category**: The provided category is stored for each flashcard and is used to name the output file.
- **Formatting**: Words in the vocabulary file are formatted for use in spaced repetition systems (with basic fields like question, answer, interval, etc.).

## Error Handling

The script will print an error message if the vocabulary file is incorrectly formatted or missing. For example:
- If a line doesn’t contain ' - ', it will be skipped.
- If the file is not found, an error will be raised.

## Testing and Validation

You can use any vocabulary file formatted as shown above to test the script. The generated JSON file can be loaded into any flashcard app that supports spaced repetition (like Anki).

### Unit Testing

To test the functionality of this script, the following unit tests are included:
- `parse_vocab_file`: Verifies correct parsing of the vocabulary file.
- `format_flashcards`: Validates that the flashcards are correctly generated based on the word pairs.

## Conclusion

This script provides an easy way to convert a vocabulary file into spaced repetition flashcards in JSON format. It supports creating flashcards for both directions (German to Hungarian and vice versa) and saves the results in a category-based JSON file.
