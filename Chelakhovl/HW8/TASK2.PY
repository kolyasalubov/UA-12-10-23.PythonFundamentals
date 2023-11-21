import re

while True:
   user_password = input("Enter your password: ")
   password_pattern = re.compile(r"^(?=.*[0-9].*)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$!%*#?&]{6,16}$")
   match = password_pattern.match(user_password)

   if match:
      print("Password is valid.")
      break
   else:
       print("Password is not valid. Please follow the specified criteria: \nAt least 1 letter between [a-z] and 1 letter between [A-Z].\nAt least 1 number between [0-9].\nAt least 1 character from [$#@].\nMinimum length 6 characters.f\nMaximum length 16 characters.")
        
