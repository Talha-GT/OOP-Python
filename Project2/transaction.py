class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount

    def __str__(self):
        return f"{self.transaction_type}: {self.amount}"
    