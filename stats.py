def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict
        