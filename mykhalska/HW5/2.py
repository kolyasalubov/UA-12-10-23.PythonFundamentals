fibo_seq = [0,1]
count = 1
while count <= 10 :
    num = fibo_seq[-1] + fibo_seq[-2]
    fibo_seq.append(num)
    count += 1

print(fibo_seq)