def count_words(book_string):
    word_count = book_string.split()
    return word_count
def num_characters(book_string):
    characters_dict = {}
    characters_count = []
    num = list(book_string)
    for i in num:
        if i.isalpha() == False:
            pass
        else:
            if i.lower() in characters_count:
                characters_dict[i.lower()] += 1
            elif i.isalpha() == True:
                characters_count.append(i.lower())
                characters_dict.update([(i.lower(), 1)])
                
    return characters_dict
def sort_on(keys):
    return keys["num"]

def sort_dict(character_dictionary):
    items = character_dictionary.items()
    sorted_dictionary = []
    for i in items:
        listing = {"char" : i[0], 
                   "num" : i[1]
                   }
        sorted_dictionary.append(listing)
    sorted_dictionary.sort(key=sort_on, reverse=True)    
    return sorted_dictionary


        
