import random

number = random.randint(1, 100)
count = 10

while count > 0:
    inp = int(input("Guess the number from 1 to 100:\n"))
    if inp == number:
        print("Good job, you win!")
        break
    else:
        if number > inp:
            print("number is greater")
        elif number < inp:
            print("number is less")
        count -= 1
        print(f"Try again. Left attempts: {count}")


