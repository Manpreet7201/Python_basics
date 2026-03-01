# file = open("geek.txt",)
# # content = file.readline()
# content = file.readlines()
# file.close()
# print(content, type(content))


file = open("geek.txt",)

# line1 = file.readline()
# print(line1, type(line1))

# line2 = file.readline()
# print(line2, type(line2))

# line3 = file.readline()
# print(line3, type(line3))

# line4 = file.readline()
# print(line4, type(line4))

line = file.readline()
while (line != ''):
    print(line,end="")
    line = file.readline()
file.close()