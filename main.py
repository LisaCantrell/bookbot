
def main():
    frank_path = "books/frankenstein.txt"
    frank_contents = get_book(frank_path)
    frank_wordcount = get_book_wordcount(frank_contents)
    # print(frank_wordcount)
    frank_char_count = get_char_count(frank_contents)
    sorted_char_list = sort_char_count(frank_char_count)
    # print(sorted_char_list)
    create_report(frank_path, sorted_char_list, frank_wordcount)

def sort_on(dict):
    return dict["num"]

def get_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_book_wordcount(book_string):
    words = book_string.split()
    count = len(words)
    return count 

def get_char_count(text_string):
    char_count = {}
    lowered_string = text_string.lower()
    for char in lowered_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count.update({char: 1})
    return char_count
            
def sort_char_count(char_dict):
    char_list = []
    for item in char_dict:
        item_dict = {"char_name": item, "num": char_dict[item]}
        char_list.append(item_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def create_report(path, sorted_char_count, word_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for char in sorted_char_count:
        char_name = char["char_name"]
        char_num = char["num"]
        print(f"The '{char_name}' character was found {char_num} times")
    print("--- End Report ---")

main()