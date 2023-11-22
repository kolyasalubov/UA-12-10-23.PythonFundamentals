import re
pattern_password = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$#]{6,16}$"

print("The password must contain \n at least 1 letter A-Z \n \
      al least 1 letter a-z \n at least 1 number \n \
      at least 1 character $#@ \n length 6-16 characters")
input_password = input("Enter the password: ")
if re.search(pattern_password, input_password) :
    print("Entered Strong Password")
else:
    print("Password not valid")