def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = word_count(text)
    num_chars = char_count(text)
    char_list = [{"letter": k, "count": v} for k, v in num_chars.items()]
    char_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")    
    for char in char_list:
        print(f"The '{char['letter']}' character was found {char['count']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def char_count(text):
    lowered_text = text.lower()
    amount = {}
    for s in set(lowered_text):
        if s.isalpha():
            amount[s] = lowered_text.count(s)
    return amount

def word_count(text):
    words = text.split()
    return len(words)

def book_text(path):
    with open(path) as f:
        return f.read()


main()