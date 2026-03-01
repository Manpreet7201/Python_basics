#  Problem 1 to craete a Animals class 

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod  # when we do not need to pass self while creating objects
    def bark():
        print("The dog is barking like, BOW BOW BOW !")

myObj = Dog()
myObj.bark()
