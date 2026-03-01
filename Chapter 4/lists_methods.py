# list methods will not create new lists , only updates them means they are mutable

# fruits = ["Tarun", "hi", 78, True, 77.90, "Sharan"]
# print(fruits)

# append method - at end
# fruits.append("Jasskaran")
# print(fruits)

# extend method - add multiple items or join lists
# fruits1 = ["True", False]
# fruits.extend("90")
# fruits.extend(fruits1)
# print(fruits)


# remove() -  removes 1st occurence
# fruits = ["Tarun", "hi", 78, True, 77.90, "Sharan", "hi"]
# fruits.remove( "hi")
# print(fruits)

# pop() - will return the last popped up item
# print(fruits.pop())
# print(fruits)
# also pop by index
# print(fruits.pop(2))
# print(fruits)

# revere() - reverse the list
fruits = ["Tarun", "hi", 78, True, 77.908, "Sharan", "hi"]
# fruits.reverse()
# print(fruits)

# sort()
# lst = [33,67,0,-2,67]
# lst.sort()
# print(lst)

# will check occurence of an item in the list
# print(fruits.count("hi"))
# print(fruits.index("hi"))
# print(fruits.index(True))

# fruits.clear()
# print(fruits)

# insert method - add an item at specific position
# fruits.insert(index, value)
fruits.insert(4, "NewItem")
print(fruits)
