def calculated_number_count(str1):
    dict_res = {}
    for i in str1:
        dict_res[i] = str1.count(i)
    return dict_res


word = input("Enter your word:\n")
result = calculated_number_count(word)
print(result)
