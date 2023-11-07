# No yelling!
def filter_words_normal(str):
    """Capitalized string and remove unneedible space"""
    str = str.split()
    str = ' '.join(str)
    str = str.capitalize()
    return str 

def filter_words_short(str):
    """Capitalized string and remove unneedible space"""
    return ' '.join(str.split()).capitalize()

# Not using any string function
def filter_words_perversion(str):
    """
    Capitalized string and remove unneedible space 
    withaut using string function
    """
    alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #alphabet_lower = list(''.join(alphabet_upper).lower())
    alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #convert string to list
    list_of_char = list(str)
    #Delite spaces
    while list_of_char[0] == ' ' :
        list_of_char.pop(0)
        
    while list_of_char[-1] == ' ' :
        list_of_char.pop(-1)
    i = 0    
    while i < len(list_of_char) :
        if list_of_char[i] == ' ' and list_of_char[i-1] == ' ':
            list_of_char.pop(i)
        else:
            i += 1    
    
            
    #Capitalized list
    for i in range(len(list_of_char)) :
        if i == 0:
            if list_of_char[i] in alphabet_lower:
                list_of_char[i] = alphabet_upper[alphabet_lower.index(list_of_char[i])]
        elif list_of_char[i] in alphabet_upper:
            list_of_char[i] = alphabet_lower[alphabet_upper.index(list_of_char[i])]

    #concatinate string from list
    result_str = ''
    for i in list_of_char :
        result_str += i
    return result_str



st = input("Enter string :")
print('Result normal function : ', filter_words_normal(st))
print('Result short function : ', filter_words_short(st))
print('Result perversion function : ', filter_words_perversion(st))