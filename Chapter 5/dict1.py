# empty dict
# student = {}


student = {
    "name": "Manpreet",
    "age": 25,
    "course": "Python",
    "marks": [200,500,345,756,300]
}

print(type(student))
print(student["name"])
print(student["marks"])
print(student["marks"][2])
student["age"] = 24
print(student.get("course"))
print(student.get("age"))