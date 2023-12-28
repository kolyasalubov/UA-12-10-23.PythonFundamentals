def count_characters(input_string):
    character_count = {}

    for char in input_string:
        char = char.lower()  # Case-insensitive counting
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1

    return character_count

# Example usage:
input_str = "hello"
result = count_characters(input_str)
print(f"Input: {input_str}")
print("Output:", result)
