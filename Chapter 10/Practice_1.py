# problem 1 , class of programmers
class Programmers():
    company = "Microsoft"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        print(f"This is the programmers class with an dunder method.Employes working at {self.company}. Employes names are {self.name}")

Emp1 = Programmers("Harshit", 34, 220000)
print(Emp1.name, Emp1.age, Emp1.salary)
Emp2 = Programmers("Inshita", 24, 120000)
print(Emp2.name, Emp2.age, Emp2.salary)

