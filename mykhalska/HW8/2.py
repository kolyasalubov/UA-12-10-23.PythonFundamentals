import re

def validate_pass(password) :
    """
Function that checks the validity of a password
func takes input from user and check whether it has 
1 upper and lower register letter,
1 number,
1 $#@ symbol
and is longer than 6 char and shorter than 16
"""
    if len(password)< 6 :
        return False
    if len(password)>16 :
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

print(validate_pass(input("Enter your password: ")))