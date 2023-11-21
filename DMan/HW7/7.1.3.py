def sum_of_char(text):
    
    """
    This function counts the numbers of characters used and 
    forms a dictionary from these values 
    """
    
    char_dict = {char : text.count(char) for char in text}
    return char_dict



    
