from stats import get_book_text, number_of_words_in_the_string, dict_of_chars, sort_dict
import sys
    

def main():
    args = sys.argv
    path = None
    try:
        path = args[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(path)
    num_of_words = number_of_words_in_the_string(text)
    dictionary = dict_of_chars(text)
    sorted_dictionary = sort_dict(dictionary)
    
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_of_words} total words
--------- Character Count -------""")
    
    for item in sorted_dictionary:
        print(f'{item['char']}: {item['num']}')
    
    print("============= END ===============")

    
main()
