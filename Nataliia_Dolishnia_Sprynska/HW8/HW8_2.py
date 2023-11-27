import re

def is_valid_password(password):
    lowercase_regex = re.compile(r'[a-z]')
    uppercase_regex = re.compile(r'[A-Z]')
    digit_regex = re.compile(r'[0-9]')
    special_char_regex = re.compile(r'[$#@]')
    
    if 6 <= len(password) <= 16:
        if lowercase_regex.search(password) and uppercase_regex.search(password) \
                and digit_regex.search(password) and special_char_regex.search(password):
            return True
        else:
            return False
    else:
        return False

user_password = input("Enter your password: ")
if is_valid_password(user_password):
    print("Password is valid.")
else:
    print("Invalid password. Please follow the specified rules.")
