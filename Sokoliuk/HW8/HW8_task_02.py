import regex as re

print("Create the password, it must be valid according to the validity rules\n")

while True:
    password = input("Input your password: ")
    if len(password) >= 6 and len(password) <= 16:
        if re.findall(r"[$#@]", password):
            if re.findall(r"\d", password):
                if re.findall(r"[A-Z]", password):
                    if re.findall(r"[a-z]", password):
                        print("Your password is valid")
                        break
                    else:
                        print("Your password must have at least 1 lowercase letter\n")
                else:
                    print("Your password must have at least 1 uppercase letter\n")
            else:
                print("Your password must have at least 1 digit\n")
        else:
            print("Your password must have at least 1 of these symbols [$, #, @]\n")
    else:
        print("Your password must consist from 6 to 16 characters\n")