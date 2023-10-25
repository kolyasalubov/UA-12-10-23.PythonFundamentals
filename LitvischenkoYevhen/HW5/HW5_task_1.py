num = [2, 5, 6, 8, 77, 6, 3, 5, 2]
count = 0
while count < len(num):
    num[count] = float(num[count])
    count += 1
print(num)