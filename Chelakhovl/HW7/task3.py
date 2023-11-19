def calculates_letters(word):
    my_dict = {}
    for i in word:
      my_dict[i]=word.count(i)
    return(my_dict)

word = input("enter a word: ")

result = calculates_letters(word)
print(result)
