from stats import get_book_text
from stats import get_num_words
from stats import get_char_count
from stats import clean_sort

import sys

def main():

    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    clean_dict = clean_sort(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in clean_dict:
        print(f"{item['name']}: {item['count']}")


main()