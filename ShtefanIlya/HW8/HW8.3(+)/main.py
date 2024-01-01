from mathematic.actions import action

print("""
      Command
Area of rectangle --> rectangle
Area of triangle --> triangle
Area of circle --> circle
      """)

act = input("Choose an action from the list above: ")
act = act.lower()
print("\n")
action(act)
