def count_characters(text):
    text = text.lower()
    char_count = {}
    
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def count_words(text):
    words = text.split()
    return len(words)

def generate_report(word_count, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    # Convert the character count dictionary to a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    
    # Sort the list by occurrences in descending order
    char_list.sort(reverse=True, key=lambda x: x["num"])
    
    # Print the character counts
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file) as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    
    generate_report(word_count, char_count)

if __name__ == "__main__":
    main()

