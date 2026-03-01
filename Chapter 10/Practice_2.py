# problem 2 , class of calculator
class Calculator():

    def __init__(self, number):
        self.number = number

    def Square(self):
        ans = self.number*self.number
        print(f"The square of {self.number} is {ans}")
    def Cube(self):
        ans = self.number*self.number*self.number
        print(f"The Cube of {self.number} is {ans}")
    def Square_root(self):
        ans = self.number ** (1/2)
        print(f"The square root of {self.number} is {ans}")

square = Calculator(4)
square.Square()
square.Cube()
square.Square_root()

