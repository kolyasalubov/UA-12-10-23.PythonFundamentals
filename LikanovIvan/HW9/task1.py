import random

tries = 0
random_num = random.randint(1,100)

while True:
    if tries < 10:
        number = int(input("Enter number here: \t"))
        if number == random_num:
            print("Congratulation!! You did it well) \n You WIN!!")
            break
        elif number < random_num:
            tries += 1
            print(f"Your number is less, try bigger one. You have {10-tries} tries left")
        elif number > random_num:
            tries += 1
            print(f"Your number is bigger, try less one. You have {10-tries} tries left")
    else:
        print("There is no tries left( \n You lose!")
        break