import random

print("""
Lets play a game!
If you win
You are free to go
otherwise...
You will be feeded
to my dogs \U0001F608     
""")

print("Guess my number from range of 1 to 100\nyou have only 10 attempts\n")

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
            print("Congratulations! You can live, for today...")
            break
        attempts -= 1
    else:
        print("You entered wrong number, silly\n")
else:
    print("Haha! You lost! my dogs will have a feast...")
