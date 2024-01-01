import random

print("Please quess the number from range of 1 to 100.\nYou have only 10 attempts\n")

attempts = 10
number_to_guess = random.randint(1, 100)

while attempts > 0:
    user_number = int(input("Guess the number: "))
    if 1 <= user_number <= 100:
        if user_number > number_to_guess:
            print("My number is less\n")
        elif user_number < number_to_guess:
            print("My number is more\n")
        else:
            if attempts == 10:
                print("No way! At the first try!\n")
            print(" Very good! You win!")
            break
        attempts -= 1
    else:
        print("You entered wrong number \n")
else:
    print("Unfortunatly, you are loser! Try again!")