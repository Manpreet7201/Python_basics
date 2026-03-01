'''
FH - process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface
''' 


f = open("geek.txt", "r")   #by default read mode
content = f.read()
print(content)
f.close()
