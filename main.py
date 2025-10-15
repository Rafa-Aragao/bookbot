from stats import count_words
from stats import num_characters
def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents =  f.read()
    return  file_contents


def main():
    Frankenstein = get_book_text("books/frankenstein.txt") # type: ignore
    Word_count = count_words(Frankenstein)
    character_count = num_characters(Frankenstein)
    
    print(f"Found {len(Word_count)} total words" )
    print(character_count)


main()
