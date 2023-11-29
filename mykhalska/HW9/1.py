import random

number = random.randint(1, 100)
count = 0

while count < 10:
    inp_num = int(input("Enter the number from 1 to 100:\n"))
    if inp_num == number:
        print("Good job, you win!")
        break
    else:
        if number > inp_num:
            print("Your number is less")
        elif number < inp_num:
            print("Your number is greather")
        count += 1
        print(f"Try again. Left attempts: {(10 - count)}")