n = int(input("Enter your number: "))
num = 1
c = n
for i in range(n):
    num *= n
    n -= 1
print(f"{c}! = {num}")
