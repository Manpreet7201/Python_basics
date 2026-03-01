class Details:
    name = "Simran"
    age = 44
    def show(self): 
        print(f"Thanks for searching- {self.name}")

class Coder:
    level = "mid-level"
    def show_level(self): 
        print(f"Your coding level is- {self.level}")


class Programmer(Details, Coder):
    lang = "Python"
    def show_info(self): 
        print(f"You are good in this language - '{self.lang}' ?")

mann2 = Programmer()
print(mann2.name, mann2.age)
# print()
mann2.show()
mann2.show_level()
mann2.show_info()

