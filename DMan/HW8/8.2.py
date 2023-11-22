def validity_of_password():
    import re
    password = input("Input your password ")

    while True:  
        if (len(password) < 6 or len(password) > 12):
            return "Invalid Password"
        elif not re.search("[A-Z]", password):
            return "Invalid Password"
        elif not re.search("[a-z]", password):
            return "Invalid Password"
        elif not re.search('\d', password):
            return "Invalid Password"
        elif not re.search("[$#@]", password):
            return "Invalid Password"
        else:
            return "Valid Password"
        
print(validity_of_password())