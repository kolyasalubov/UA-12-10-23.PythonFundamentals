
login = "First"
chance = 5
print("You have 5 chance to enter a login")
while chance > 0:
    user_login = input("Enter a login: ")
    if user_login == login:
        print('Welcome')
        break
    else:
        chance -= 0
        print("Your chance left")


