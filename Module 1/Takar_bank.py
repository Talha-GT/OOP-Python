class bank:
    def __init__(self,Balance):
        self.Balance=Balance
        self.min_transation=50
        self.max_transation=100000

    def depostite(self,ammount):
        self.Balance+=ammount

    def withdraw(self,ammount):
        if ammount<self.min_transation:
            print('Vai tui ki eto fokir je eto kom taka withdraw korsis')
        elif ammount>self.max_transation:
            print(f'vai tor {ammount} taka bank dite parbe na karon tui maximum {self.max_transation} taka uthaite parbi')
        else :
            self.Balance-=ammount
            print(f'vai apni {ammount} taka uthaicen apner current balance{self.Balance}' )

    def current_balance(self):
        print(f"Current balance: {self.Balance}")


Janata=bank(50000)
Janata.depostite(1000)
Janata.current_balance()
Janata.withdraw(25)
Janata.withdraw(10000000)
Janata.withdraw(10000)
Janata.current_balance()