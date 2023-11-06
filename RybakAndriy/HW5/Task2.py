numbers_fib = int(input("entered number n: "))

dict_a, dict_b = 0, 1

print("Fibonacci numbers:")
while dict_a <= numbers_fib:
    print(dict_a)
    dict_a, dict_b = dict_b, dict_a + dict_b