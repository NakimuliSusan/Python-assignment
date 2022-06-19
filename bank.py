from datetime import datetime
from unicodedata import name
class Account:
    def __init__(self,account_name,number):
        self.account_name = account_name
        self.number = number
        self.balance = 0
        self.withdraws = []
        self.deposits = []
        self.combination = []
        self.transaction_charge = 100
        self.loan_balance = 0
      
        

    def deposit(self,amount):
        if amount <= 0:
            return f"depositing amount must be greater than zero"
        else:
          date = datetime.now()
          self.balance += amount
          self.deposits.append(amount)
          details = {"date": date.strftime('%Y/%m/%d %H:%M'), "amount": amount, "narration": f"Deposit"}
        #   self.deposits.append(details) 
          self.combination.append(details)
        #   print(self.deposits)
          return f"Hello {self.account_name} you have deposited {amount} and your balance is {self.balance}"

    
    def withdraw(self,amount):
        date = datetime.now()
        withdraw_amount = self.balance - self.transaction_charge
        if amount <= 0:
            return f"Enter the correct amount"
        elif amount > self.balance:
            return f"your account balance is low "
        elif withdraw_amount > self.balance:
            return "Insufficient funds to withdraw"
        else:
   
           self.balance -= amount
           self.balance -= self.transaction_charge
           withdraws = {"date": date.strftime('%Y/%m/%d %H:%M'), "amount": amount, "narration": f"Withdraw"}
           withdraw_details = f"You withdrew KSHS{amount}, and your new account balance was {self.balance}"
           self.withdraws.append(withdraws)
           self.combination.append(withdraws)
           print(withdraw_details)
        #    print(self.withdraws)
        #    print(self.combination)
        #    return f"Hello {self.account_name} you have withdrawn {amount} and your balance is {self.balance}"

    def deposits_statement (self):
        for deposits in self.deposits:
            print(f"{deposits}")

    def withdraw_statement (self):
        for withdraw in self.withdraws:
            print(withdraw)

    def get_balance (self) :
        return f"Your account balance is {self.balance}"

    def full_statement (self) :
        for item in self.combination :
            self.combination.sort(key=lambda item: item['date'], reverse=True)
            date = item['date']
            amount = item['amount']
            narration = item['narration']
            print(f"{date}----------- {narration}----------- {amount}")

    def borrow(self,amount):
        count = sum(self.deposits)
        qualification = (count) * 1/3
        amount += (amount)* 0.03
        if amount <= 100:
            return f"Enter amount more than 100"
        elif self.loan_balance > 0:
            return f"You have an outstanding amount of {self.loan_balance}"
        elif amount >= qualification:
            return f"You cannot borrow more than {count//3}"
        elif len(self.deposits)< 10:
            return f"You must have deposited more than 10 times "
        else:
            self.loan_balance += amount
            return f"Your loan balance is {self.loan_balance}"

    def loan_repayment(self, amount):
        if amount < self.loan_balance:
            self.loan_balance -= amount
            return f"You have paid {amount} and your have an outstanding balance of {self.loan_balance}"

        else:
            self.loan_balance-=amount
            overpay = amount - self.loan_balance
            self.balance+=overpay
            return f"You loan has been fully settled."
    def transfer(self, amount, account):
        if amount > self.balance:
            return f"Your account balance is too low cannot transfer amount"
        elif amount <= 0:
            return f"Enter correct amount" 
        else:
            self.balance-= amount
            account.balance += amount
            return f"You have sent {amount} to {account.account_name} and your balance is {self.balance}"

       
        

       


       

          


            



        
            
