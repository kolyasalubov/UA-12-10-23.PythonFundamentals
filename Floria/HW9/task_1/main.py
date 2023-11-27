
from random import randint


number = randint(1, 100)

tries = 0

print("Welcome to the number guessing game!")
print("I have chosen a number between 1 and 100.")
print("You have 10 tries to guess it.")

while tries < 10:
    guess = int(input("Enter your guess: "))

    tries += 1

    if guess == number:
        print("You guessed it! The number was", number)
        print("You took", tries, "tries to guess it.")
        break
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")

if tries == 10:
    print("Sorry, you ran out of tries.")
    print("The number was", number)