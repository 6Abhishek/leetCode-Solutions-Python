def length_of_longest_substring(s):

    start = 0  # Left edge of the window
    max_length = 0  # Maximum length found so far
    char_index_map = {}  # Stores the most recent index of each character

    for i, char in enumerate(s):  # i is the right edge of the window
        if char in char_index_map and char_index_map[char] >= start:
            # Duplicate found within the current window
            start = char_index_map[char] + 1  # Shrink the window

        char_index_map[char] = i  # Update the character's index
        max_length = max(max_length, i - start + 1)  # Update max_length

    return max_length

no_of_unique_char=length_of_longest_substring("pwwkew")
print(no_of_unique_char)