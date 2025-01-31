class Admin:
    def __init__(self, bank):
        self.bank = bank

    def menu(self):
        while True:
            print("\n1. Create Account")
            print("2. Delete Account")
            print("3. View All Accounts")
            print("4. View Total Bank Balance")
            print("5. Toggle Loan Feature")
            print("6. Exit Admin Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter name: ")
                email = input("Enter email: ")
                account_type = input("Enter account type (Savings/Current): ")
                self.bank.create_user(name, email, account_type)
            elif choice == "2":
                print("Feature not implemented yet.")
            elif choice == "6":
                break
            else:
                print("Invalid choice!")
