class Employee:
    a = 1
class Programmer(Employee):
    a  = 44
    b = 10
class Details(Programmer):
    c = 111

my_obj = Employee()
print(my_obj.a)
my_obj = Programmer()
print(my_obj.a)
print(my_obj.b)

my_obj = Details()
print(my_obj.a)