def number_of_characters(word):
    dict_ = {}
    for i in word:
        if i in dict_:
            dict_[i]+=1
        else:
            dict_[i]= 1

    return dict_
