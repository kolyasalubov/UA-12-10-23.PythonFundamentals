#Reversing Words in a String
def revers_str(str):
    """Reversing Words in a String"""
    #str = str.split()
    #str = reversed(str)
    #str = ' '.join(str)
    #return str
    return ' '.join(reversed(str.split()))

input_string = input("Enter string :")
print('Reversing words in a string : ', revers_str(input_string))