import random

# class Train:
#     def book_ticket(self, train_no, fro, to):
#         print(f"Ticket is booked from {fro} to {to} for the train no {train_no} .")
        
#     def get_status(self, train_no):
#         print(f"Ticket is booked for the train no {train_no} .")

#     def get_fare(self, train_no, fro, to):
#         print(f"Ticket fare is {random.randint(220,5555)} from {fro} to {to} for the train no {train_no} .")


# myObj = Train()
# myObj.book_ticket(126612, "Up" , "Delhi")
# myObj.get_status(126612)
# myObj.get_fare(126612, "Up" , "Delhi")


class Train:
    def __init__(self, train_no):
        self.train_no = train_no
    
    def book_ticket(self, fro, to):
        print(f"Ticket is booked from {fro} to {to} for the train no {self.train_no} .")
        
    def get_status(self):
        print(f"Ticket is booked for the train no {self.train_no} .")

    def get_fare(self, fro, to):
        print(f"Ticket fare is {random.randint(220,5555)} from {fro} to {to} for the train no {self.train_no} .")


myObj = Train(126612)
myObj.book_ticket("Up" , "Delhi")
myObj.get_status()
myObj.get_fare("Up" , "Delhi")