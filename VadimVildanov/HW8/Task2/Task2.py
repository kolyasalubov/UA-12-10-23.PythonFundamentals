import re


def validate_password(password):
    if len(password) < 6:
        return False
    if len(password) > 16:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True


string = input("Enter your password: ")
print(validate_password(string))