def count_words(book_string):
    word_count = book_string.split()
    return word_count
def num_characters(book_string):
    characters_dict = {}
    characters_count = []
    num = list(book_string)
    for i in num:
        if i.lower() == " ":
            pass
        else:
            if i.lower() in characters_count:
                characters_dict[i.lower()] += 1
            elif i.isalpha() == True:
                characters_count.append(i.lower())
                characters_dict.update([(i.lower(), 1)])
                
    return characters_dict

def sort_dict(character_dictionary):
    sorted_keys = sorted(character_dictionary.items())
    sorted_dict = dict(sorted_keys)
    return sorted_dict


