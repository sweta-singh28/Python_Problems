f = open("demo.txt", "r")
data = f.read()

#to read the data line by line
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)

print(data)

f.close