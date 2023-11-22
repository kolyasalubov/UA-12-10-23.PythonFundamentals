# I create function with argument "word". "word" is word which will enter user.
def calculates_characters(word):
    # I decided do with dict and save letters
    dict = {}
    # Iterate through each letters in "word"
    for letters in word:
        # I want to get keys(they will show how many times letters is in user words
        keys = dict.keys()
        """"
        Check if "letters" is already a key in the dict? and if letters is already a key in the dict - we have 2 key
        ("hello"- l:2 key, because it met twice)
        """
        if letters in keys:
            dict[letters] += 1
        # If "letters" isn't a key, add it to the dict, and it has 1 key("hello"- o:1 key, because it met first
        else:
            dict[letters] = 1
    return dict


string = input("Enter your word: ")
print(calculates_characters(string))