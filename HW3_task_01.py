file = open("Python_philosophy.txt", "r")
text = file.read()
file.close()
processing = text.split()

print(f"There are {processing.count("better")} occurences of the word 'better'\n")
print(f"There are {processing.count("never")} occurences of the word 'never'\n")
print(f"There are {processing.count("is")} occurences of the word 'is'\n")

text = text.split('\n')
for line in text:
    line = line.replace("i", "&")
    line = line.upper()
    print(line)