# No yelling!
def filter_words(str):
    str = str.split()
    str = ' '.join(str)
    str = str.capitalize()
#   str = ' '.join(str.split()).capitalize()
    return str 

st = input("Enter string :")
print(filter_words(st))