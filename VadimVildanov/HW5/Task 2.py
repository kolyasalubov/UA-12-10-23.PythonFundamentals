number_fibonacci = int(input("Enter your limit: "))
variable_1 = 0
variable_2 = 1
variable_3 = variable_2
count = 1
while count <= number_fibonacci:
    variable_1, variable_2 = variable_2, variable_3
    variable_3 = variable_1 + variable_2
    print(variable_3, end=" ")
    count += 1
print()

