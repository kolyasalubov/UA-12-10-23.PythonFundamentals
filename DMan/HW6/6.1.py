            #EVEN NUMBERS WHICH ARE DEVISEBLE BY 2

l1 = [i for i in range(1, 11) if i%2 == 0]  
print(l1)
            #ODD NUMBERS WHICH ARE DEVISIBLE BY 3
                     #impractical variant

l2 = []
for i in range(11):
    if i%3 == 0:
        if i%2 != 0:
            l2.append(i)
print(l2)
                     #simple variant

l1 = []
for i in range(1, 11, 2):              
    if i%3==0:
       l1.append(i)
print(l1)

                     #another one
l1 = [i for i in range(1, 11, 2) if i%3 == 0]
print(l1)                                


             # NUMBERS THAT ARE NOT DEVISIBLE BY 2 AND 3

l1 = [i for i in range(1, 11, 2) if i%3 != 0]
print(l1)
