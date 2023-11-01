num = int(input("Enter any four digit number : "))

digit = num
product = 1

while digit > 0 :

    product = product * (digit % 10)

    digit = int(digit / 10)

ascending = "".join(sorted(str(num)))

print("Product of all digits in", num, ":", product)
print(str(num)[::-1])
print("Sorted list od digits the included in the number: ",ascending )