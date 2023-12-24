import random

user_name = input("Hello! What is your name?\n")
number = random.randint(1, 40)
counter = 10

while counter > 0:
    guess_number = int(input("\nEnter your number: "))
    counter -= 1

    if guess_number == number:
        print(f"{user_name} is the winner, congratulations!!!")
        break
    elif 1 <= guess_number <= 40 and guess_number < number and counter > 0:
        print("Your number is less, try again...\n"
              f"{counter} more attempts left\n")
    elif 1 <= guess_number <= 40 and guess_number > number and counter > 0:
        print("Your number is more, try again...\n"
              f"{counter} more attempts left\n")
    elif not 1 <= guess_number <= 40 and counter > 0:
        print("Your number is not in range!!! Try again\n"
              f"{counter} more attempts left\n")
else: 
    print("Sorry, you have used all the attempts\n" 
          f"The correct number was {number}\n" 
          f"Better luck next time, {user_name}!")