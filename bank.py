import logging

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            logging.log(msg="Insufficient funds", level=logging.INFO)
            print("Insufficient funds")
        else:
            self.balance -= amount
    def display_balance(self):
        print(self.balance)
        return self.balance
