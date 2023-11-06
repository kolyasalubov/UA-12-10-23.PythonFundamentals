even = [i for i in range(1,11) if i%2==0]
odd = [i for i in range(1,11) if i%2==1 and i%3==0]
not_divisible = [i for i in range(1,11) if i%2!=0 and i%3!=0]
print(even,odd,not_divisible)