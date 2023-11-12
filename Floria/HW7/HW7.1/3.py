def number_count(str1):
    dict = {}
    for i in str1:
        dict[i] = str1.count(i)
    return print (dict)


word = input("Enter arandom word:\n")
number_count(word)
