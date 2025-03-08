def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    character_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in character_dict:
            character_dict[lowered_char] += 1
        else: 
            character_dict[lowered_char] = 1
    return character_dict

def sort_on(dict):
    return dict["count"]

def sort_chars(char_dict):
    sorted_chars = []
    for char in char_dict:
        item = {"char": char, "count": char_dict[char]}
        sorted_chars.append(item)
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
