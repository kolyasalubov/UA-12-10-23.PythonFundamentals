zen = str("""The Zen of Python, by Tim Peters\
1.Beautiful is better than ugly.\
2.Explicit is better than implicit.\
3.Simple is better than complex.\
4.Complex is better than complicated.\
5.Flat is better than nested.\
6.Sparse is better than dense.\
7.Readability counts.\
8.Special cases aren't special enough to break the rules.\
9.Although practicality beats purity.\
10.Errors should never pass silently.\
""")
print(zen)

print(("amound of better"), zen.count('better'))
print(zen.count('never'))
print(zen.count('is'))

print(zen.upper())
new_zen = zen.replace('i', '&')
print(new_zen)