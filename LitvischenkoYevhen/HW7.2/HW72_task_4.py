#Convert a Number to a String!
def convert_to_str(num: int):
    """convert int to str diferent metods"""
    st_1 = str(num)
    print('srt(object) ',st_1, type(st_1))
    st_2 = f'{num}'
    print('f\'{object}\' ',st_2, type(st_2))
    st_3 = '{}'.format(num)
    print('\'{}\'.format(object)',st_3, type(st_3))

input_num = int(input('Enter the number: '))
convert_to_str(input_num)