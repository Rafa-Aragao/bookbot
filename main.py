from stats import count_words
from stats import num_characters
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents =  f.read()
    return  file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    terminal = sys.argv[1]
    Frankenstein = get_book_text(terminal) # type: ignore
    Word_count = count_words(Frankenstein)
    character_count = num_characters(Frankenstein)
    character_dict = sort_dict(character_count)
    
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {len(Word_count)} total words" )
    print("--------- Character Count -------")
    for i in character_dict:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")



main()
