l1 = []
for i in range (1,11):
    if i%2 == 0:
        l1.append(i)
print(f"Even numbers that are divisible by 2: {l1}")

l2 = []
for item in range (1,11):
    if item%3 == 0 and item%2 ==1:
        l2.append(item)
print(f"odd numbers, which are divisible by 3: {l2}")

l3 = []
for it in range (1,11):
    if it%3 != 0 and it%2 != 0:
       l3.append(it)
print(f"numbers that are not divisible by 2 and 3: {l3}")


list1 = [x for x in range(1,11) if x%2 == 0]
print(f"Even numbers that are divisible by 2: {list1}")

list2 = [x for x in range(1,11) if x%3 == 0 and x%2 ==1]
print(f"odd numbers, which are divisible by 3: {list2}")

list3 = [x for x in range(1,11) if x%3 != 0 and x%2 != 0]
print(f"numbers that are not divisible by 2 and 3: {list3}")
