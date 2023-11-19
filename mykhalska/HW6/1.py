div_by_2 = []
div_by_3 = []
not_div_by_2_3 = []

num = range(1,11)
for n in num :
    if n%2 == 0 :
        div_by_2.append(n)
    if n%3 == 0 :
        div_by_3.append(n)
    if n%2 and n%3 != 0 :
        not_div_by_2_3.append(n)

print(div_by_2)
print(div_by_3)
print(not_div_by_2_3)