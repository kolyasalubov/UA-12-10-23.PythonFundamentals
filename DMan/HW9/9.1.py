from random import randint

print("Hi! You have a chance to guess the number in ten attemps!")
print("The number ranges from 1 to 100\nGood luck!")

comp_num = randint(1, 100)
users_num = int(input("Enter your number"))
count = 0

while count < 9:
    if comp_num != users_num:
        print("Wrong.\nTry again!")
        users_num = int(input("Enter number "))
        count += 1
    elif comp_num == users_num:
        print("Amazing!\n" 
             +"Your intuition and luck are second to none!")
        break
    else:
        print("Invalid input. Enter valid numbers, please")
        count += 1
    if count == 9:
        print("You have used all ten attemps.\n"
              +"The number was: ", comp_num)
       