import re


def is_valid_password(password):

    # Check length
    if 6 <= len(password) <= 16:
        # Check for at least 1 lowercase letter, 1 uppercase letter, 1 number, and 1 character from [$#@]
        if (re.search("[a-z]", password)
                and re.search("[A-Z]", password)
                and re.search("[0-9]", password)
                and re.search("[$#@]", password)):
            return True
    return False


print("Please create a password with: at least 1 lowercase letter, at least 1 uppercase letter, at least 1 number, and 1 character from [$#@]")
user_password = input("Please create your password: ")


if is_valid_password(user_password):
    print("Your password is valid.")
else:
    print("Your password is invalid.")