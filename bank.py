class Account:
    def __init__(self,account_name , balance):
        self.account_name = account_name
        self.balance = balance
        

    def deposit(self,amount):
        self.balance += amount
        return f"Hello {self.account_name} you have deposited {amount} and your balance is {self.balance}"

    
    def withdraw(self,amount):
        self.balance -= amount
        return f"Hello {self.account_name} you have withdrawn {amount} and your balance is {self.balance}"
