
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_dict = count_chars(file_contents)
    char_list = sort_dict(char_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for letter in char_list:
        print(f"The {letter["name"]} character was found {letter["count"]} times")
    print("--- End report ---")


def count_words(text_to_count):
    words = text_to_count.split()
    return(len(words))

def count_chars(text_to_count):
    text_to_count = text_to_count.lower()
    text_to_count = text_to_count.replace(' ','')
    #print(text_to_count)
    chars = {}
    for x in text_to_count:
        if x in chars.keys():
            chars[x] = chars[x] + 1
        else:
            chars[x] = 1
    return(chars)

def sort_key(item_to_sort):
    return(item_to_sort["count"])

def sort_dict(char_dict):
    char_list = []
    print(char_dict)
    for key,val in char_dict.items():
        if key.isalpha():
            li = { "name": key, "count": val }
            char_list.append(li)

    char_list.sort(reverse=True, key=sort_key)
    return(char_list)

main()
