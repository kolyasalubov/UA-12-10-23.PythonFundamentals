def long_fun():
    n = int(input("Enter count digital: "))
    res = ""
    lst = []
    if n == 0:
        print("No digital")
    if n == 1:
        lst.insert(0, 0)
        print(lst)
    if n == 2:
        lst.insert(0, 0)
        lst.insert(1, 1)
        print(lst)
    if n > 2:
        lst.insert(0, 0)
        lst.insert(1, 1)
        for i in range(n - 2):
            c = lst[i + 1] + lst[i]
            lst.append(c)

    for i in lst:
        res += str(i)
        res += ", "
    res = res[:-2]
    print(res)


def short_fun():
    n = int(input("Enter count digital: "))
    c = 0
    b = 1
    d = []
    for i in range(n):
        d.append(c)
        c = b + d[i] - c
        b = c + d[i]
    print(d)


while True:
    answer = int(input("If you want big code enter 1, but, if you want short code enter 2.\n1 or 2?\n"))
    if answer == 1:
        break
    elif answer == 2:
        break


if answer == 1:
    long_fun()
elif answer == 2:
    short_fun()
