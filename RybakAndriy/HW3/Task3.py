a = int(input("Enter digit a:"))
b = int(input("Enter digit b:"))
print("a= ", a, "; b= ", b, sep="")

a = int(input("Enter digit a:"))
b = int(input("Enter digit b:"))
a, b = b, a
print("a= ", a, "; b= ", b, sep="")

a = int(input("Enter digit a:"))
b = int(input("Enter digit b:"))
a = a + b
b = a - b
a = a - b
print("a= ", a, "; b= ", b, sep="")