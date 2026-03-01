# class Employee:
#     a = 1
#     def show(self):
#         print(f"The value of a is {self.a}.")

# e = Employee()
# e.a = 45  # instance attribute will be printed
# e.show()


class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}.")

e = Employee()
e.a = 45  # class attribute will be printed, even created instance attribute
e.show()