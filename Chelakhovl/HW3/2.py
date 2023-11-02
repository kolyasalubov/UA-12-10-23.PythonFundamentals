#вирішив задачу за допомогою зрізів
task2 = input("Enter your number in 1000 for 9999:")

number1 = task2[0:1]
number2 = task2[1:2]
number3 = task2[2:3]
number4 = task2[3:4]
number5 = int(number1)
number6 = int(number2)
number7 = int(number3)
number8 = int(number4)

number9 = number5*number6*number7*number8

print(number9)

#ЗАДАЧА 2
number10 = task2[::-1]
print(number10)

#задача 3
number11 = ''.join(sorted(task2))

print(number11)
 
