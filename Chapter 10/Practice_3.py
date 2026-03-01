# Problem 3
class myClass:
    a = "Hii"

myObj = myClass()
print(myObj.a)  # prints class attribute becoz instance attr is not present
myObj.a = "Not Hii"
print(myObj.a)  # prints instance attribute becoz instance attr is present
print(myClass.a) # prints class attribute - means does not changed the class attr