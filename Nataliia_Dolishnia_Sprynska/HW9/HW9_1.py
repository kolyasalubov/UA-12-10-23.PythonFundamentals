import random

def guessing_game():
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Guessing Game! You have 10 attempts to guess the number.")

    for attempt in range(1, 11):
        user_guess = int(input(f"Attempt {attempt}: Enter your guess (between 1 and 100): "))

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
            break
        elif user_guess < secret_number:
            print("The secret number is greater. Try again.")
        else:
            print("The secret number is smaller. Try again.")

    else:
        print(f"Sorry, you've used all 10 attempts. The secret number was {secret_number}.")

guessing_game()
