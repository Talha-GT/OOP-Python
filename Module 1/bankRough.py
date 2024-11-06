class Bank:
    def __init__(self, Balance):
        self.Balance = Balance
        self.min_transaction = 50
        self.max_transaction = 100000

    def deposit(self, amount):
        self.Balance += amount
        print(f"{amount} taka deposited. Current balance: {self.Balance}")

    def withdraw(self, amount):
        if amount < self.min_transaction:
            print("Vai tui ki eto fokir je eto kom taka withdraw korsis")
        elif amount > self.max_transaction:
            print(f"vai tor {amount} taka bank dite parbe na karon tui maximum {self.max_transaction} taka uthaite parbi")
        else:
            self.Balance -= amount
            print(f"vai apni {amount} taka uthaicen apner current balance {self.Balance}")

    def current_balance(self):
        print(f"Current balance: {self.Balance}")

# Testing the class
Janata = Bank(50000)
Janata.deposit(1000)
Janata.current_balance()
Janata.withdraw(25)
Janata.withdraw(10000000)
Janata.withdraw(10000)
Janata.current_balance()
