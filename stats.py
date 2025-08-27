def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def number_of_words_in_the_string(str):
    words = str.split()
    num_of_words = len(words)
    return num_of_words

# def dict_of_chars(str):
#     dict_obj = {}
#     for char in str:
#         lower_char = char.lower()
#         if lower_char in dict_obj:
#             dict_obj[lower_char] += 1
#         else:
#             dict_obj[lower_char] = 1
#     return dict_obj

# def dict_of_chars(s):
#     lower_s = s.lower()
#     return { char : lower_s.count(char) for char in set(lower_s)}

def dict_of_chars(s):
    lower_s = s.lower()
    return {char: lower_s.count(char) for char in set(lower_s) if char.isalpha()}


def sort_dict(char_dict):
    def sort_on(items):
        return items["num"]    
    array = [{"char": key, "num": value} for key, value in char_dict.items()]
    sorted_array = sorted(array, reverse=True, key=sort_on)
    return sorted_array
  
   