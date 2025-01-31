import random
from transaction import Transaction

class User:
    def __init__(self, name, email, account_type):
        self.name = name
        self.email = email
        self.password = "password123"  
        self.account_number = random.randint(100000, 999999)
        self.account_type = account_type
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount))
        print(f"Deposited {amount}. Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded!")
        else:
            self.balance -= amount
            self.transactions.append(Transaction("Withdrawal", amount))
            print(f"Withdrew {amount}. Current Balance: {self.balance}")

    def transfer(self, target_account, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred {amount} to {target_account.name}.")
