py_philosophy = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never .
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea – let's do more of those!"""

#--------First task-----------
#First sollution
# print('Number of words of "better":', py_philosophy.count('better'))
# print('Number of words of "never":', py_philosophy.count('never'))
# print('Number of words of "is":', py_philosophy.count('is'))

#Second sollution
philosophy = py_philosophy.lower()
philosophy = py_philosophy.split()

count_bet = 0
count_nev = 0
count_is = 0

for i in philosophy:
    if i == 'better':
        count_bet += 1
    elif i == 'never':
        count_nev += 1
    elif i == 'is':
        count_is += 1

print(f'In python philosophy we can find: \n 1){count_bet} words "better" \n 2){count_nev} words "never" \n 3){count_is} words "is"')

#--------Second task-----------
print(py_philosophy.upper())

#--------Third task-----------
print(py_philosophy.replace('i', '&'))