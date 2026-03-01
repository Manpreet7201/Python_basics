class Employee:
    def __init__(self):
        print("Constructor of Employee.")
    a = 1
class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer.")
    a  = 44
    b = 10
class Details(Programmer):
    # can also use super class constructors
    def __init__(self):
        super().__init__()
        print("Constructor of Details.")
    c = 111

# my_obj = Employee()
# print(my_obj.a)
my_obj = Programmer()
print(my_obj.a, my_obj.b)
# my_obj = Details()
# print(my_obj.a,my_obj.b,my_obj.c)