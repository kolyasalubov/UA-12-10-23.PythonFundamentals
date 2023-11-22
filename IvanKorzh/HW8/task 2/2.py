import re

while True:
    password = input("Create your password:\n")
    if len(password) >= 6:
        if len(password) <= 16:
            if len(re.findall("[a-z]", password)) >= 1 and len(re.findall("[A-Z]", password)) >= 1:
                if len(re.findall("[0-9]", password)) >= 1:
                    if len(re.findall("[@#$]", password)) >= 1:
                        print("Your password is valid")
                        break
                    else:
                        print("Your password not contain @, # or $")
                else:
                    print("Your password not contain 0-9")
            else:
                print("Your password not contain A-Z and a-z")
        else:
            print("Your password long than 16")
    else:
        print("Your password less than 6")

