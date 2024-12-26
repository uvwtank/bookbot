def sort_on(dict):
    return dict["num"]

def count_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_count(text):
    return len(text.split())

def get_text(path_to_text):
    with open(path_to_text) as f:
        return f.read()

def main():
    text_path = "books/frankenstein.txt"
    text = get_text(text_path)
    text_count = get_count(text)
    chars_dict = count_characters(text)
    print(f"--- Begin report of {text_path} ---")
    print(f"{text_count} words found in the document")
    print("")
    for char, count in chars_dict.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print(f"--- End Report ---")
main()