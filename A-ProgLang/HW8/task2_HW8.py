import re

def validate_password(password):
    if 6 <= len(password) <= 16:
        if re.search("[a-z]", password):
            if re.search("[A-Z]", password):
                if re.search("[0-9]", password):
                    if re.search("[$#@]", password):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

user_password = input("Enter password: ")

if validate_password(user_password):
    print("Password is valid")
else:
    print("The password is invalid")
