number = input("input youre number")
a = int(number[-4])
b = int(number[-3])
c = int(number[-2])
d = int(number[-1])
first = a * b * c * d
second = number[::-1]
print(first, second)
