# string="1234"
# total=0
#
# for i in string:
#     if i.isdigit():
#         total=total+int(i)
#
# print(total)
############################################
def second_most_used_character(s):
    # Initialize dictionaries to store character frequencies
    frequency = {}

    # Iterate through each character in the string
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in frequency:
            frequency[char] += 1
        # Otherwise, initialize its count to 1
        else:
            frequency[char] = 1

    # Sort the dictionary by values (frequencies) in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1],reverse=True)
    print(sorted_frequency)

    # If there are less than two unique characters, return None
    if len(sorted_frequency) < 2:
        return None

    # Return the second most used character
    return sorted_frequency[1][0]


# Example usage:
string = "banananbn"
print("Second most used character:", second_most_used_character(string))
