# default(implicit) order
default_order = "Hello {}, {} and {}".format('John','Bill','Sean')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print(positional_order)
# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print(keyword_order)
