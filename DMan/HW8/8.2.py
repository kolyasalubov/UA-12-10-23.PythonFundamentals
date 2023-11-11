def validity_of_password():
    import re
    p= input("Input your password  ")

    while True:  
        if (len(p)<6 or len(p)>12):
            return "Invalid Password"
        elif not re.search("[a-z]",p):
            return "Invalid Password"
        elif not re.search("[0-9]",p):
            return "Invalid Password"
        elif not re.search("[A-Z]",p):
            return "Invalid Password"
        elif not re.search("[$#@]",p):
            return "Invalid Password"
        else:
            return "Valid Password"
        
print(validity_of_password())