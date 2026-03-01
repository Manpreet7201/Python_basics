class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def Balance(self):
        return self._balance
    
    @Balance.setter
    def Balance(self, value):
        if value<0:
            print("Invalid Balance.")
        else:
            self._balance = value
    
obj = BankAccount(1000)
print(obj.Balance)
obj.Balance = -500
obj.Balance = 2000
print(obj.Balance)