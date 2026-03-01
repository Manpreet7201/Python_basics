class Details:
    # class attribuites
    name = "Simran"  # class attribute 
    age = 20

    # class methods
    def getInfo(self):  # passing the object as self parameter 
        print(f"The name is {self.name} and the age is {self.age}. Thanks for searching.")

    # static methods , we dont need to pass obj. as self paramter
    @staticmethod
    def StaticMethod():
        print("This is an static method, where we do not need to pass the self paramter.")


mann = Details()
mann.getInfo()  #object is passed but not seeing in actual
# Details.getInfo(mann)

mann.StaticMethod()  # static method call
