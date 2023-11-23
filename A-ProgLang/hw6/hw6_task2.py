valid_login = {'First'}
user_login = input("Enter your login: ")
while user_login not in valid_login:
    print("Error: Invalid login")
    user_login = input("Try again: ")
print(f"Congratulations, {user_login}!")