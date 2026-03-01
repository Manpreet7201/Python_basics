class Details:
    name = "Simran"
    age = 20

    def __init__(self, name, age): 
        self.name = name
        self.age = age
        print(f" Thanks for searching- {name}")

mann = Details("Jass", 44)
print(mann.age)
