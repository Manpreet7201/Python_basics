# Create a dictionary from two lists (keys & values).
mylist1 = ["Manpreet", "Kiran", "Japneet"]
mylist2 = [95.00, 85.00, 75.56]
myDict = {}
for i in range(0, len(mylist1)):
    myDict[mylist1[i]] = mylist2[i]

print("My Dictionary- ", myDict)


#    ooooooooooooo rrrrrrrrrrrrrrrrrr
myDict = dict(zip(mylist1, mylist2))
# print("My Dictionary- ", myDict)

