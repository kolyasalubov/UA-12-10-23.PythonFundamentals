even_num_devisible_2 = evnum = []
for num in range(1, 11):
    if num % 2 == 0:
        evnum.append(num)
print (evnum)

odd_num_devisible_3 = odnum = []
for num in range(1, 11):
    if num % 3 == 0:
        odnum.append(num)
print (odnum)

num_not_devisible_2_and_3 = notdev = []
for num in range(1, 11):
    if num % 2 != 0 and num % 3 != 0:
        notdev.append(num)
print (notdev)
