from user import User

class Bank:
    def __init__(self):
        self.users = []
        self.admin_password = "admin123"
        self.is_loan_enabled = True

    def create_user(self, name, email, account_type):
        user = User(name, email, account_type)
        self.users.append(user)
        print(f"Account created for {name} with Account Number: {user.account_number}")

    def login_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None

    def login_admin(self, password):
        return password == self.admin_password
