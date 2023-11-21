natural_number = int(input("\nPlease enter a four-digit number: "))
print("\nYour number is",natural_number)

natural_digits_list = list(repr(natural_number))
natural_digits_join = '*'.join(natural_digits_list)
natural_digits_eval = eval(natural_digits_join)
print(f"\nThe product of the number {natural_number} ="
      ,natural_digits_eval)

reversed_of_digits = repr(natural_number)[::-1]
reversed_of_digits_int = int(reversed_of_digits)
print(f"\nReverse of the number {natural_number} ="
      ,reversed_of_digits_int)

number_in_list = repr(natural_number)
sorted_numbers = sorted(number_in_list)
digits_join = ''.join(sorted_numbers)
sort_digits_int = int(digits_join)
print(f"\nDigits in ascending order of number {natural_number} ="
      ,sort_digits_int)
print()