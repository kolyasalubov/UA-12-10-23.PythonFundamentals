# num_1 = 0
# num_2 = 1

# n = int(input("How many Fibonacci numbers do you want to see?  "))
# counter = 0

# while counter < n:
#      print(num_1, end = "  ")
#      num_sum = num_1 + num_2
#      num_1 = num_2
#      num_2 = num_sum
#      counter += 1
# print("\n")

# num_1 = num_2 = 1
# n = int(input("How many Fibonacci numbers do you want to see?  "))
 
# for i in range(2, n):
#     num_sum = num_1 + num_2
#     num_1 = num_2
#     num_2 = num_sum
#     print(num_2, end=' ')

def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("How many Fibonacci numbers do you want to see? "))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))
# honestly found it on the internet
