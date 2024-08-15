"""
2. Write a Python program to create a class representing a bank. 
Include methods for managing customer accounts and transactions.
"""

class Bank:
    def __init__(self):
        self.acc  = {}  # acc no. as key

    def create_account(self, acc_num, name):
        if acc_num in self.acc:
            print("Account  already exists")

        else:
            self.acc[ acc_num] = {'name' : name, 'balance': 0}

    def deposit(self, acc_num, amount):
        if acc_num not in self.acc:
            print( "Account not found")

        else:
            self.acc[ acc_num]['balance'] +=amount

    def withdraw(self, acc_num, amount):
        if acc_num not in self.acc:
            
            print("Account not found")
        elif self.acc[acc_num]['balance'] <amount:
            print("Insufficient balance")
        else:
            self.acc[acc_num]['balance'] -=amount

    def check_balance(self, acc_num):
        if acc_num not in self.acc:
            print("Account not found")
        else:
            balance = self.acc[acc_num]['balance']
            print("remainig balance:", balance)


bank = Bank()
bank.create_account("101", "abc")
bank.create_account("102", "xyz")
bank.deposit("101", 200)
bank.withdraw("102", 100)
bank.check_balance("101")
bank.check_balance("105")
