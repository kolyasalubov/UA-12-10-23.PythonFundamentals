factorial = int(input("Enter factorial: "))
if factorial < 0:
    print("Error!")
elif factorial == 0:
    print(f"{factorial}! = 1")
else:
    i = 0
    f = 1
    text = "1"
    while i < factorial:
        i += 1
        f = f * i
        print(str(i))
        text = text + " * " + str(i)
    print(f"{factorial}! = {text} = {f}")
