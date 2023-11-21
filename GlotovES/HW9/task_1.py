import random

def guessing_game():

    secret_number = random.randint(1, 100)
    
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("You have 10 tries to guess the correct number.")

    for attempt in range(1, 11):
        user_guess = int(input(" Enter your guess: "))

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempt} tries.")
            break
        elif user_guess < secret_number:
            print("Your number is less then mine. Try again!")
            print(f"You have {10-attempt} attempt") 
        else:
            print("Your number is bigger then mine. Try again!")
            print(f"You have {10-attempt} attempt")

    else:
        print(f"Sorry, you've run out of attempts {attempt}. The correct number was {secret_number}.")


guessing_game()
