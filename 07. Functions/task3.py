"""Task3. Write a function that calculates the number of characters included in
given string
• input: "hello"
• output: {"h":1, "e":1,"l":2,"o":1}"""

def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_str = "hello"
print(count_characters(input_str))
