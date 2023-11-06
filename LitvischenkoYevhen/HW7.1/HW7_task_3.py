def count_char(str):
    """
    calculates the number of characters in string
    """
    #select unique chars
    unique_chars = set(str)
    #create dict
    chars_dict = {}.fromkeys(unique_chars, 0)
    #calculate number of characters in string
    count_of_char = {x: str.count(x) for x in chars_dict}
    return count_of_char

counted_string = input("Enter the counted string: ")
print('Calculated characters :', count_char(counted_string))


