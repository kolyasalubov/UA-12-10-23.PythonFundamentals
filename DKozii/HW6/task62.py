login = " "
while login != "First":
    login = input("Enter your login: ")
    if login == "First":
        print(f"Hello {login}")
    else:
        print("Error login, enter right login!")
