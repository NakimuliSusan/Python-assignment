class Account:
    def __init__(self,account_name,number):
        self.account_name = account_name
        self.number = number
        self.balance = 0
        self.withdraws = []
        self.deposits = []
        self.transaction_charge = 100
      
        

    def deposit(self,amount):
        if amount <= 0:
            return f"depositing amount must be greater than zero"
        else:
          self.balance += amount
          self.deposits.append(amount)
        #   self.deposits.append(self.balance)
          print(self.deposits)
          return f"Hello {self.account_name} you have deposited {amount} and your balance is {self.balance}"

    
    def withdraw(self,amount):
        if amount <= 0:
            return f"Enter the correct amount"
        elif amount > self.balance:
            return f"your account balance is low "
        else:
           self.balance -= amount
           actual_balance = self.balance - self.transaction_charge
           self.withdraws.append(amount)
        #    self.withdraws.append(self.balance)
           print(self.withdraws)
           return f"Hello {self.account_name} you have withdrawn {amount} and your balance is {actual_balance}"

    def deposits_statement (self):
        for deposits in self.deposits:
            print(f"You deposited KES {deposits}.")

    def withdraw_statement (self):
        for withdraw in self.withdraws:
            print(f"You withdrew KES{withdraw} and your balance is {self.balance- self.transaction_charge} with a charge {self.transaction_charge}.")

    def get_balance (self) :
        return f"Your account balance is {self.balance- self.transaction_charge}"
            
