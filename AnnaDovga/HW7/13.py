def word(word_1):
    '''
    Calculates the number in a given string
    param word_1 --> str
    return dictionary --> dict
    '''

    dictionary = {}
    word_1 = word_1.lower()
    dictionary = {i: word_1.count(i) for i in word_1 if i not in dictionary}
    return dictionary

print(word(input('Print the word ')))
