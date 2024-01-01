import random

def number_guessing_game():
    secret_number = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100. Can you guess it in 10 tries?")

    for attempt in range(1, 11):
        user_guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
