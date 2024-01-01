import re

password = input("Enter your password: ")
password_length = len(password)
upper_a_z = re.findall('[A-Z]', password)  # >> [P A S S W O R D]
lower_a_z = re.findall('[a-z]', password) # >> [p a s s w o r d]
digits = re.findall("\d", password) # >> [1 2 3 4 5 6 7 8 9 0]
spec_symbols = re.findall(r'[@ # $]', password) # >> [@ # $ % ...]

#PaSSw0Rd@123
# compare_upper = list(set(password) & set(upper_a_z)) # >> [P S S R]
# compare_lower = list(set(password) & set(lower_a_z)) # >> [a w d]
# compare_digits = list(set(password) & set(digits)) # >> [1 2 3 0]
# compare_spec_symbols = list(set(password) & set(spec_symbols)) # >> [@]

if password_length < 8 or password_length > 16:
    print("Password must be 8-16 characters long!")
elif upper_a_z == [] or lower_a_z == []:
    print("Password must contain uppercase (A-Z) and lowercase (a-z) letters!")
elif digits == []:
    print("Password must contain at least 1 digit!")
elif spec_symbols == []:
    print("Password must contain at least 1 character from [@#$]")
else:
    print(f"Your password is {password}")
