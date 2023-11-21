LETTERS = "abcdefghijklmnopqrstuvwxyz"
CAPS_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMS = "1234567890"
CHARS = "$#@"

def if_valid(password):
    global LETTERS
    global CAPS_LETTERS
    global CHARS
    global NUMS
    is_lett = False
    is_caps = False
    is_nums = False
    is_char = False

    if 6 <= len(password) <= 16:
        for char in password:
            if char in LETTERS:
                is_lett = True
            elif char in CAPS_LETTERS:
                is_caps = True
            elif char in CHARS:
                is_char = True
            elif char in NUMS:
                is_nums = True

        if is_lett and is_caps and is_char and is_nums:
            return True
        else: 
            if not is_lett:
                print("Your password does not contain any letter")   
            if not is_caps:
                print("Your password does not contain any capital letter") 
            if not is_char:
                print("Your password does not contain any special char") 
            if not is_nums:
                print("Your password does not contain any number") 
    else: print("Your password must contain from 6 to 16 symbols")
    return False

while True:
    password = input("Enter your password: \t")
    if if_valid(password):
        break

print("Congratulation, your password was accepted")


