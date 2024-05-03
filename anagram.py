def is_anagram(s1, s2):
    # If the lengths of the strings are different, they cannot be anagrams
    if len(s1) != len(s2):
        return False

    # Create dictionaries to store the frequency of characters in each string
    char_count_s1 = {}
    char_count_s2 = {}

    # Count the frequency of characters in the first string
    for char in s1:
        char_count_s1[char] = char_count_s1.get(char, 0) + 1

    # Count the frequency of characters in the second string
    for char in s2:
        char_count_s2[char] = char_count_s2.get(char, 0) + 1

    # Compare the dictionaries to check if they are anagrams
    return char_count_s1 == char_count_s2


# Example usage:
s1 = "listen"
s2 = "silent"
print("Are '{}' and '{}' anagrams?".format(s1, s2), is_anagram(s1, s2))
