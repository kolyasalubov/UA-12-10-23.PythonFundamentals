"""
Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:
- Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!
Tim sighed, healready knew it's gonna be a long day.
Few hours later, boss came again:
Much better - he said - but now I want to change that class name to SecondUsefulClass,
and wentoff. Although Timmy had no idea why changing name is so important for his boss,
he realized, that it's not the end, so he turned to you, his guru, to help him and asked you to prepare some function,
which could change name of given class.
Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers),
but starting only with upper case letter. In other case it should raise an exception.
Disclaimer: there are obviously betters way to check class name than in example cases, but let's stick with that,
that Timmy yet has to learn them.
"""


def class_name_changer(old_class, new_name):
    # Check if the new class name follows the specified rules
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError(
            "Invalid class name. It should start with an uppercase letter and contain only alphanumeric characters.")

    # Create a new class with the desired name
    new_class = type(new_name, old_class.__bases__, dict(old_class.__dict__))

    return new_class


# Example usage:
class MyClass:
    pass


# Change the class name from MyClass to UsefulClass
UsefulClass = class_name_changer(MyClass, "UsefulClass")

# Change the class name from UsefulClass to SecondUsefulClass
SecondUsefulClass = class_name_changer(UsefulClass, "SecondUsefulClass")

# Test the new class name
obj = SecondUsefulClass()
print(type(obj).__name__)  # Output: SecondUsefulClass
