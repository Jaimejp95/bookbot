import sys
from stats import count_words, count_chars, sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]  # Get the book path from command-line arguments
    text = get_book_text(filepath)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    char_counts = count_chars(text)
    print(char_counts)
    sorted_chars = sort_char_count(char_counts)
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {char_dict['count']}")
    
    print("============= END ===============")

main()