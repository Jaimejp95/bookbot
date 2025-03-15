def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_count(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})
    
    # Sort using a lambda function
    char_list.sort(reverse=True, key=lambda dict: dict["count"])
    
    return char_list