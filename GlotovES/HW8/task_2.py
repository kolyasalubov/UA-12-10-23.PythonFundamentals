import re

def valid_password(password):
    
    if 6 <= len(password) <= 16:
        
        if re.search("[a-z]", password):
            
            if re.search("[A-Z]", password):
                
                if re.search("[0-9]", password):
                    
                    if re.search("[$#@]", password):
                        return True
                    else:
                        print("Password must contain at least one character from [$, #, @].")
                else:
                    print("Password must contain at least one digit [0-9].")
            else:
                print("Password must contain at least one uppercase letter [A-Z].")
        else:
            print("Password must contain at least one lowercase letter [a-z].")
    else:
        print("Password must be between 6 and 16 characters.")

    return False


user_password = input("Enter your password: ")
if valid_password(user_password):
    print("Password is valid.")
else:
    print("Password is not valid.")

