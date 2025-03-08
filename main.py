def get_book_text(book):
    content_string = ""
    with open(book) as content:
        content_string = content.read()
    return content_string
import sys

from stats import get_num_words

from stats import get_num_chars

from stats import sort_chars

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text_string = get_book_text(sys.argv[1])
        word_count = get_num_words(text_string)
        chars = get_num_chars(text_string)
        char_count = sort_chars(chars)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for current_dict in char_count:
            character = current_dict["char"]
            count = current_dict["count"]
            if character.isalpha() == True:
                print(f"{character}: {count}")
        print("============= END ===============")
    
main()
    
