import random

attempt = 0
random_num = random.randint(1,100)

while True:
    if attempt < 10:
        number = int(input("Enter your number: "))
        if number == random_num:
            print("Congratulation! \n You win!")
            break
        elif number < random_num:
            attempt += 1
            print(f"Your number is bigger you used {attempt} from 10 attemps")
        elif number > random_num:
            attempt += 1
            print(f"Your number is lees you used {attempt} from 10 attemps")
    else:
        print(f"There is no attempt left( \n You lose! The number was {random_num}")
        break
