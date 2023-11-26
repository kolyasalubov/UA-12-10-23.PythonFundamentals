def calculates_the_number_of_characters(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count [letter] = 1   
    print(letter_count)
    return letter_count
word = "hello"
result = calculates_the_number_of_characters(word)
