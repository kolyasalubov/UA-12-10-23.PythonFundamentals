python_philosophy = """
Find separately the number of occurrences of the words
"better" "never" and "is" in the given line.
You need to display all text in uppercase (all letters in uppercase).
Replace all occurrences of the symbol "i" with "&".
"""

text_in_uppercase = python_philosophy.upper()
text_with_i_replaced = text_in_uppercase.replace("I", "&")

count_better = text_with_i_replaced.count("BETTER")
count_never = text_with_i_replaced.count("NEVER")
count_is = text_with_i_replaced.count("IS")

print(text_with_i_replaced)
print(f"Occurrences of 'BETTER': {count_better}")
print(f"Occurrences of 'NEVER': {count_never}")
print(f"Occurrences of 'IS': {count_is}")

