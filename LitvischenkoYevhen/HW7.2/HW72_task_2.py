 #Find The Distance Between Two Points
def distans(a, b:->list):
    """
    input -> list

    """
    return ((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5

first_ordered_pair = list(map(int, input("Enter first pair (space between them) :").split()))
second_ordered_pair = list(map(int, input("Enter second pair :").split()))
print(f'Distans between ordered pairs :{distans(first_ordered_pair, second_ordered_pair):2.2f}')
