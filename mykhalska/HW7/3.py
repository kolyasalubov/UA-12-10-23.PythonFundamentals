#7.3
def calculate_char(word) :
    """
    This function accepts a string, count the number of characters included
    in the string and return the values
    """
    char_dict = {i : word.count(i) for i in word}
    return print(char_dict)
    
word = input("Enter your word: ")    
calculate_char(word)