def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
def get_book_text(path):
    word_counter = 0
    letter_counter = 0
    character_dictionary = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
        'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
        's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,
        '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
    }

    with open(path) as f:
        for word in f.read().split():
            word_counter += 1
            for letter in word.lower():
                if letter in character_dictionary:
                    character_dictionary[letter] += 1
        return character_dictionary

main()
