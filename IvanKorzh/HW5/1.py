import random
lst = []
n = int(input("Enter count elements in list: "))
for i in range(n):
    lst.append(random.randint(0, 10))
print(lst)
for el in range(len(lst)):
    lst[el] = float(lst[el])
print(lst)
