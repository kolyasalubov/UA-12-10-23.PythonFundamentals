l = []
while True:
    element = input("Enter an element: ")
    if element == "stop" or element == "STOP":
        break
    elif element.lstrip('-').isdigit():
        l.append(int(element))
    else:
        print("""If you wish to stop the loop,
just input \"stop\" or \"STOP\"""")

l_div_for_2 = []
l_div_for_3 = []
l_not_two_three = []
aqq = []
print(f"List: {l}\n")

for el in l:
    if el == 0:
        continue
    elif el % 3 == 0:
        l_div_for_3.append(el)
    elif el % 2 == 0:
        l_div_for_2.append(el)
    else:
        l_not_two_three.append(el)
print(f"""List of numbers divisible by 2:
{l_div_for_2} \n""")
print(f"""List of numbers divisible by 3:
{l_div_for_3} \n""")
print(f"""List of numbers not divisible by 2 and 3:
{l_not_two_three} \n""")
