correct_login = "First"
login_successful = False

while not login_successful:
    user_login = input("Enter your login: ")

    if user_login == correct_login:
        print("Hello, user!")
        login_successful = True 
    else:
        print("Error: Incorrect login. Try again.")
