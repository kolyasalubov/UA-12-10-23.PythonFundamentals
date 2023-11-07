#Will you make it?
def check_fuil(fuil, distans):
    """
    possible to get to the pump or not
    fuil -> int
    distance -> int
    return true if it is possible and false if not
    """
    fuel_consumption = 25
    if fuil*fuel_consumption >= distans:
        return True
    else:
        return False

fuin_in_tank = int(input("Enter fuil in the tank : "))
distans_to_pump = int(input("Enter distans to pump : "))
if check_fuil(fuin_in_tank, distans_to_pump) :
    print("It's time to refuel")
else:
    print("Take a walk )))")