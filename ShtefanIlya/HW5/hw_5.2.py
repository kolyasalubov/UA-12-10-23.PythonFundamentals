# 0 1 1 2 3 5 8 13
border = int(input("Enter a border:"))
i = 0
j = 0
res = 1
text = "0"
while i < border:
    res = res + j  # 1+0=1 1+1=2 3+2=5
    j = j + res  # 0+1=1 1+2=3 3+5 = 8
    i += 1
    text = text + ", " + str(res) + ", " + str(j)
    print(res, j, " ", f"({i}) - iteration")
print("Fibonacci numbers:", text)
