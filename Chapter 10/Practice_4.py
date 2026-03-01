# problem 2 , class of calculator
class Calculator():

    def __init__(self, number):
        self.number = number

    def Square(self):
        ans = self.number*self.number
        print(f"The square of {self.number} is {ans}")
    
    @staticmethod
    def Greet():
        print("Hello , good morning.")

square = Calculator(4)
square.Square()
square.Greet()  #


