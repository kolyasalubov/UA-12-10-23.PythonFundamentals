#####################################

str_37 = 'If the implementation is easy to explain, it may be a good idea'

#####################################

if str_37.find('better') >= 0:
    print(str_37.find('better'))
else:
    print('"better" is not exist in this string')

if str_37.find('never') >= 0:
    print(str_37.find('never'))
else:
    print('"never" is not exist in this string')

if str_37.find('is') >= 0:
    print(str_37.find('is'))
else:
    print('"is" is not exist in this string')

#####################################

print(str_37.upper())

#####################################

print(str_37.replace('i','&'))
