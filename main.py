from stats import count_words
from stats import num_characters
from stats import sort_dict
def get_book_text(filepath):
    with open(filepath) as f: 
        file_contents =  f.read()
    return  file_contents


def main():
    Frankenstein = get_book_text("books/frankenstein.txt") # type: ignore
    Word_count = count_words(Frankenstein)
    character_count = num_characters(Frankenstein)
    character_dict = sort_dict(character_count)
    
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {len(Word_count)} total words" )
    print("--------- Character Count -------")
    print(character_dict)
    print("============= END ===============")



main()
