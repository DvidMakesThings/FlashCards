import json
import argparse

# Function to read and parse the vocabulary file
def parse_vocab_file(file_path):
    word_pairs = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Skip empty lines and lines that don't contain ' - '
            line = line.strip()
            if not line or ' - ' not in line:
                continue
            
            german, hungarian = line.split(' - ')
            word_pairs.append((german.strip(), hungarian.strip()))
    
    return word_pairs

# Function to format the data as required
def format_flashcards(word_pairs, category):
    formatted_cards = []
    
    for german, hungarian in word_pairs:
        formatted_cards.append({
            "question": german,
            "answer": hungarian,
            "interval": 2,
            "last_review": None,
            "score": 0,
            "category": category
        })
        formatted_cards.append({
            "question": hungarian,
            "answer": german,
            "interval": 2,
            "last_review": None,
            "score": 0,
            "category": category
        })
    
    return formatted_cards

# Main function to parse the file and generate JSON
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate flashcards from vocabulary file.")
    parser.add_argument('--file', required=True, help="Path to the vocabulary file.")
    parser.add_argument('--category', required=True, help="Category for the flashcards.")
    args = parser.parse_args()

    # Parse the vocabulary file
    word_pairs = parse_vocab_file(args.file)

    # Format the word pairs into flashcards
    formatted_flashcards = format_flashcards(word_pairs, args.category)

    # Convert the result to JSON format
    formatted_json = json.dumps(formatted_flashcards, ensure_ascii=False, indent=4)

    # Print to console (for verification)
    print(formatted_json)

    # Sanitize category name: replace spaces with underscores
    sanitized_category = args.category.replace(' ', '_')

    # Save the JSON data to a file named after the category (no "flashcards" in the filename)
    output_file = f'{sanitized_category}.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(formatted_json)

    print(f"Flashcards have been saved to {output_file}")

# Run the script
if __name__ == "__main__":
    main()
