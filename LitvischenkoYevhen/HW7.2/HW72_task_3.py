# No yelling!
def filter_words_normal(str):
    str = str.split()
    str = ' '.join(str)
    str = str.capitalize()
    return str 

def filter_words_short(str):
    return ' '.join(str.split()).capitalize()

# Not using any string function
def filter_words_perversion(str):
    alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #alphabet_lower = list(''.join(alphabet_upper).lower())
    alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    list_of_char = list(str)
    #Delite space
    i = 0    
    while i < len(list_of_char) :
        if i == 0 and list_of_char[i] == ' ' :
            list_of_char.pop(0)
        elif list_of_char[i] == ' ' and list_of_char[i-1] == ' ':
            list_of_char.pop(i)
        else:
            i += 1    

    #Capitalized list
    for i in list_of_char :
        index_of_char = list_of_char.index(i)
        if (index_of_char == 0):
            if i in alphabet_lower:
                list_of_char[0] = alphabet_upper[alphabet_lower.index(i)]
        elif i in alphabet_upper:
            list_of_char[index_of_char] = alphabet_lower[alphabet_upper.index(i)]

    #concatinate strinf from list
    result_str = ''
    for i in list_of_char :
        result_str += i
    return result_str


st = input("Enter string :")
print('Result normal function : ', filter_words_normal(st))
print('Result short function : ', filter_words_short(st))
print('Result perversion function : ', filter_words_perversion(st))