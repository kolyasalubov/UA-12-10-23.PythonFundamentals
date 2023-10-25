num = int(input('Enter the number: '))
fi = [0, 1]
count = 2
while count <= num:
    fi.append(fi[count-1]+fi[count-2])
    count +=1
print(f'{num} = {fi}')
