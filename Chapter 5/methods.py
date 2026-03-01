# student = {
#     "name": "Manpreet",
#     "age": 25,
#     "course": "Python",
#     "marks": [200,500,345,756,300],
#     45:"HII"
# }


# print(student["marks"][2])
# student["age"] = 24
# print(student.get("course"))
# print(student.get("age"))

# items() method - will give the list of all key-values
# print(student.items())

#  keys()
# print(student.keys())
# values()
# print(student.values())

# update({})  - for updating and adding key-values
# print(student.update({"name":"Reena"}))
# print(student.update({"name":"Manpreet","class":"VII"}))
# student["skills"] = "Dance"

# get()
# print(student.get("age"))
# print(student.get("age1"))  #return(none) good way to get values
# print(student["age"])
# print(student["age1"])   # give key error



# student = {
#     "name": "Manpreet",
#     "age": 25,
#     "course": "Python",
#     "marks": [200,500,345,756,300],
#     45:"HII"
# }

# pop() - will return the value of the popped up key
# print(student.pop("age"))
# print(student)

# popitem() - removes and return last key-value item
# print(student.popitem())
# print(student)

# removes all items
# print(student.clear())
# print(student)


student = {
    "name": "Manpreet",
    "age": 25,
    "course": "Python",
    "marks": [200,500,345,756,300],
    45:"HII"
}
# copy() - make an duplicate dictionary
# student1 = student.copy()
# print(student)
# print(student1)

# fromkeys() - Create dictionary with same value for all keys
myKeys = {"Name", "Age", "Course"}
newdict = dict.fromkeys(myKeys, "NA")
print(newdict)

