import random
class Train:
    def __init__(slf, train_no):
        slf.train_no = train_no
    
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