# number = int(input("Enter your factorial: "))
# fact = 1
# for i in range(2, number + 1):
#     fact = fact * i
# print("The factorial of ", number, " is: ", fact)

input_number = int(input("Input natural number: "))

fact = 1

if input_number == 1 or input_number == 0:
 print("Factorial {}! =".format(input_number), fact)
elif input_number < 0:
 print("Factorial non positive number don't exist")
else:
    for item in range(1,input_number + 1):
        fact *= item
print("Factorial {}! =".format(input_number), fact)