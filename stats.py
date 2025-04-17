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

def clean_sort(char_dict):
    list_dict = []
    for k, v in char_dict.items():
        if k.isalpha():
            list_dict.append({'name':k, 'count':v})
    # clean_dict = list_dict.sort()
    clean_dict = sorted(list_dict, key=lambda d: d['count'], reverse=True)
    return clean_dict
