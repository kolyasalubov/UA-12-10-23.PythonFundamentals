#Counting sheep...
def sheep_count(arr):
    if arr :
        return arr.count(True)


sheep_arrow = []
#sheep_arrow = [True,  True,  True,  False,
#            True,  True,  True,  True ,
#            True,  False, True,  False,
#            True,  False, False, True ,
#            True,  True,  True,  True ,
#            False, False, True,  True]

print(f"Sheep present : {sheep_count(sheep_arrow)}")