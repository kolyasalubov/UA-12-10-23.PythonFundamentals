# dict_of_login = {"Student": ["John", "Marie", "Henry"], "Mentor": "Luigi", "Tech support": "Alice"}

# while True:
#     login_name = input("Enter your login: ")

#     keys = list(dict_of_login.keys())

#     if login_name in keys:
#         if login_name == keys[0]:
#             print(f"Welcome {login_name}")
#             break
#         else:
#             raise ValueError("You do not have rights to authorise on this login!")
#     else:
#         print("There is no such position")


tuple_of_logins = ("First", "Second", "Third")

while True:
    login_name = input("Enter your login: ")

    if login_name in tuple_of_logins:
        if login_name == "First":
            print(f"Welcome {login_name}")
            break
        else:
            print("Error! You are not First!\n")
            break
    else: 
        print("There is no such login name\n")
    
