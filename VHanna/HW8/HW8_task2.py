def check_password(password):
    if not (6 <= len(password) <= 16):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char in "$#@]" for char in password):
        return False

    return True

if __name__ == "__main__":
    user_password = input("Enter your password: ")

    if check_password(user_password):
        print("Password is valid.")
    else:
        print("Invalid password. Try again.")
