even_num_devisible_2 = evennum = []
for num in range(1, 10):
    if num % 2 == 0:
        evennum.append(num)
print (evennum)

odd_num_devisible_3 = oddnum = []
for num in range(1, 10):
    if num % 3 == 0:
        oddnum.append(num)
print (oddnum)

num_not_devisible_2_and_3 = notdevisible = []
for num in range(1, 10):
    if num % 2 != 0 and num % 3 != 0:
        notdevisible.append(num)
print (notdevisible)
