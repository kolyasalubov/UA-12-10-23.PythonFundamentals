def amount_of_num(string):
    d = {}
    for el in string:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    return d


s = input("Enter a text: ")
print(amount_of_num(s))
