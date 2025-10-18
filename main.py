import sys
from stats import get_num_words, get_num_character, sort_dictionary

def get_book_text(path_to_file):
    with open(path_to_file,'r') as f:
        file_contents = f.read()
        return file_contents

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]



book = get_book_text(file_path)
total_words = get_num_words(book) 
total_letters = get_num_character(book)
sorted_letters = sort_dictionary(total_letters)

# Report Format
print("============ BOOKBOT ============")
print(f"Analyzing book found at {file_path}...")
print("----------- Word Count ----------")
print(f"Found {total_words} total words")
print("--------- Character Count -------")
for item in sorted_letters:
    print(f"{item['char']}: {item['num']}")