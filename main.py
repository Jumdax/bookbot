def read_file(filename):
    """
    Opens the file in read mode and returns its contents as a string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def count_words(text):
    """
    Splits the text string on whitespace and returns the number of words.
    """
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Converts the text to lowercase and returns a dictionary with
    the count of each character in the text.
    """
    text = text.lower()  # Convert to lowercase
    char_dict = {}
    for char in text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict


def sort_character_frequencies(freq_dict):
    """
    Takes a dictionary of character frequencies (e.g., {'a': 10, 'b': 3, ...})
    and returns a list of dictionaries in the format:
    [
        {"letter": "a", "num": 10},
        {"letter": "b", "num": 3},
        ...
    ]
    sorted in descending order by "num".
    """
    # 1. Convert the dictionary to a list of dictionaries
    freq_list = []
    for letter, count in freq_dict.items():
        if letter.isalpha():
            freq_list.append({"letter": letter, "num": count})
    
    # 2. Sort in descending order based on the "letter" key
    freq_list.sort(reverse=True, key=lambda item: item["letter"])
    
    return freq_list

def main():
    filename = "books/frankenstein.txt"
    # Read the entire file
    text = read_file(filename)
    
    # Print the contents of the file
    print("=== File Contents ===")
    print(text)
    print("=====================")

    # Count the words in the text
    total_words = count_words(text)
    
    # Print the word count
    print(f"\nThe file '{filename}' contains {total_words} words.")

    #  Count character frequencies in the text
    char_counts = count_characters(text)
    print("\nCharacter frequencies (lowercased):")
    print(char_counts)

    # Use the function to get a sorted list of character frequencies
    sorted_frequencies = sort_character_frequencies(char_counts)
    
    # Print the result
    for item in sorted_frequencies:
        print(f"The '{item['letter']}' character was found {item['num']} times")


if __name__ == "__main__":
    main()

