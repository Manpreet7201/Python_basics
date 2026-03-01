class Details:
    name = "Simran"
    age = 20

    def show(self): 
        print(f"Thanks for searching- {self.name}")

class Programmer(Details):
    name = "Jasspreet"
    age = 34
    def show_info(self): 
        print(f"Thanks for searching the age- {self.age}")

mann1 = Details()
mann2 = Programmer()
print(mann1.age, mann1.name, mann2.name, mann2.age)
# print()
mann2.show()
mann2.show_info()

