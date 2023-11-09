correct_login = "First"
attempts = 3
print("You have only 3 attempts to enter a login!")
while attempts > 0: 
    user_login = input("Enter a login: ")
    if user_login == correct_login:
        print('Welcome!')
        break
    else:
        attempts -= 1
        print(f"{attempts} attempts left.")       
if attempts == 0:
    print("Your attempts have been run out")
    























