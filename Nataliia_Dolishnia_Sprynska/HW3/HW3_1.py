zen_of_python = """
Beautiful is better than ugly.
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
There should be one-- and preferably only one --obvious way to do it.[a]
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.[b]
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea – let's do more of those!
"""

occurrences_better = zen_of_python.lower().count("better")
occurrences_never = zen_of_python.lower().count("never")
occurrences_is = zen_of_python.lower().count("is")

line_uppercase = zen_of_python.upper()
line_with_replacement = zen_of_python.replace('i', '&')

print(f"Occurrences of 'better': {occurrences_better}")
print(f"Occurrences of 'never': {occurrences_never}")
print(f"Occurrences of 'is': {occurrences_is}")
print(f"All text in uppercase: {line_uppercase}")
print(f"Line with 'i' replaced by '&': {line_with_replacement}")



