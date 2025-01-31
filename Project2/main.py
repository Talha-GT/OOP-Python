from bank import Bank
from admin import Admin
from user import User

def main():
    bank = Bank()
    while True:
        print("\n1. User Login")
        print("2. Admin Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            user_email = input("Enter email: ")
            user_password = input("Enter password: ")
            user = bank.login_user(user_email, user_password)
            if user:
                user.menu()
            else:
                print("Invalid credentials!")
        elif choice == "2":
            admin_password = input("Enter admin password: ")
            if bank.login_admin(admin_password):
                Admin(bank).menu()
            else:
                print("Invalid admin password!")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
