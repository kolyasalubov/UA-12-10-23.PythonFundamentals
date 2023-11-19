def num_char(lst):
    result = {}
    for i in lst:
        result[i] = lst.count(i)
    return result    


word = input('Enter your word: \t')
print(num_char(word))

