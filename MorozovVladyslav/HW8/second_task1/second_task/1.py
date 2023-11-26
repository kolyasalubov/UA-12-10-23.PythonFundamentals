import re
password = input('ENter your password: ')
PATTERN1 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$#]{6,16}$'
def is_valid_password(password):
    '''Checks if password is valid'''
    return True if re.match(PATTERN1,password) else False

print(is_valid_password(password))

print(is_valid_password('A123@das')) # True
print(is_valid_password('asdsadd1')) # False
print('======================')
#second variantion
def is_valid_password1(password):
    '''Checks if password is valid'''
    length1 = len(password)>=6
    length2 = len(password)<=16
    small_letter = bool(re.search(r'[a-z]',password))
    big_letter = bool(re.search(r'[A-Z]',password))
    digit = bool(re.search(r'[0-9]',password))
    special_character = bool(re.search(r'[#@$]',password))

    return all(length1,length2,small_letter,big_letter,digit,special_character)

print(is_valid_password(password))

print(is_valid_password('A123@das')) # True
print(is_valid_password('asdsadd1')) # False
