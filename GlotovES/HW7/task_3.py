def calculate_character_count(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


user_input = input("Enter a string: ")
character_count = calculate_character_count(user_input)
    
print("Result:", character_count)
