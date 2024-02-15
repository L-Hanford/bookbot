import time

def main():
    #Variables - path and character_dictionary which will be used to count each character within the provided text
    book_path = "books/frankenstein.txt"
    character_dictionary = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
            'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
            's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,
            '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
                            }

    #Finds the total amount of words within the provided text
    read_text = get_book_text(book_path)
    #Generates the reader object which allows us to iterate through the provided text
    word_counter = book_word_counter(read_text)
    #Generates the character counter as compared to the dictionary provided above vs the text provided
    character_counter = book_character_counter(read_text,character_dictionary)
    #Provides a sorted dict of occurrences of characters within provided text
    character_counter_sorted = report_printer(character_counter) 
    
    for entry in character_counter_sorted:
        i = 0
        print(f"{entry["char"]} {entry["num"]} ")
        i += 1

def get_book_text(path_to_text):
    with open(path_to_text) as book:
        return book.read()

def book_word_counter(text):
    words = text.split()
    return len(words)

def book_character_counter(text,character_dictionary):
    for character in text.lower():
        if character in character_dictionary:
            character_dictionary[character] += 1
    return character_dictionary

def sort_on_counter(d):
    return d["num"]
    
def report_printer(characters_counted_dict):
    sorted_characters = []
    for character in characters_counted_dict:
        sorted_characters.append({"char": character, "num": characters_counted_dict[character]})
    sorted_characters.sort(reverse=True,key=sort_on_counter)
    return sorted_characters

main()