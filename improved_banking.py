class Banking:
    def __init__(self, user_name, initial_balance):
        self.name = user_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Successfully deposited {amount}."
        else:
            return "Deposit amount must be positive."

    def get_balance(self):
        return f"Account Name: {self.name} | Current Balance: {self.balance}"

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Successfully withdrew {amount}."
            else:
                return "Insufficient balance."
        else:
            return "Withdrawal amount must be positive."


def banking_app():
    account = None

    while True:
        print("\n***** Simple Banking App *****")
        print("0. Create Account")
        print("1. Check Balance")
        print("2. Deposit Balance")
        print("3. Withdraw Balance")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 4.")
            continue

        if choice == 0:
            if account:
                print(f"An account already exists for {account.name}.")
            else:
                name = input("Enter account holder name: ")
                try:
                    initial_balance = float(input("Enter initial balance: "))
                    if initial_balance < 0:
                        print("Initial balance must be non-negative.")
                    else:
                        account = Banking(name, initial_balance)
                        print(f"Account created successfully for {name} with a balance of {initial_balance}.")
                except ValueError:
                    print("Invalid balance amount.")

        elif choice == 1:
            if account:
                print(account.get_balance())
            else:
                print("No account found. Please create an account first.")

        elif choice == 2:
            if account:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    print(account.deposit(amount))
                except ValueError:
                    print("Invalid deposit amount.")
            else:
                print("No account found. Please create an account first.")

        elif choice == 3:
            if account:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    print(account.withdraw(amount))
                except ValueError:
                    print("Invalid withdrawal amount.")
            else:
                print("No account found. Please create an account first.")

        elif choice == 4:
            print("Thank you for using the Simple Banking App. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 4.")


if __name__ == "__main__":
    banking_app()
