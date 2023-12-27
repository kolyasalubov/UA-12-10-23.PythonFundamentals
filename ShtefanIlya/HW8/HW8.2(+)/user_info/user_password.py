import re

def check_password(password):
    
    password_length = len(password)
    upper_a_z = re.findall('[A-Z]', password) 
    lower_a_z = re.findall('[a-z]', password)
    digits = re.findall("\d", password)
    spec_symbols = re.findall(r'[@ # $]', password)
    
    compare_upper = list(set(password) & set(upper_a_z)) 
    compare_lower = list(set(password) & set(lower_a_z))
    compare_digits = list(set(password) & set(digits))
    compare_spec_symbols = list(set(password) & set(spec_symbols))
    
    if password_length < 8 or password_length > 16:
        print("Password must be 8-16 characters long!")
    elif compare_upper == [] or compare_lower == []:
        print("Password must contain uppercase (A-Z) and lowercase (a-z) letters!")
    elif compare_digits == []:
        print("Password must contain at least 1 digit!")
    elif compare_spec_symbols == []:
        print("Password must contain at least 1 character from [@#$]")
    else:
        print(f"Your password is {password}")

