def main():
    book_path = "books/frankenstein.txt"
    file_contents = read_file(book_path)
    word_count = get_word_count(file_contents)
    char_count = get_char_count(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(char_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")



def get_word_count(file):
    file_split = file.split()
    return len(file_split) # return the number of words in the file

def read_file(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def get_char_count(word_list):
    char = {}
    for word in word_list:
        lower_word = word.lower()
        for letter in lower_word:
            if letter in char:
                char[letter] += 1
            else:
                char[letter] = 1
    return char

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()