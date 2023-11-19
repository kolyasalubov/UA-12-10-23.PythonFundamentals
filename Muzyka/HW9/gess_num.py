import random

num = random.randint(1,100)
attempts = 0
max_attempts = 9
while attempts < max_attempts:
    num_gess = int(input("please, guess the number between 1 and 100\n"))
    if attempts == max_attempts:
        print("you loose, the number was:", num)
        break
    elif num == num_gess:
        print("You win! number was:", num)
        break
    elif num < num_gess:
        print("your number is higher")
        attempts += 1
    elif num > num_gess:
        print("your number is lover")
        attempts += 1
