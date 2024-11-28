class Banking:
    def __init__(self, user_name, initial_balance):
        self.name = user_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return amount

    def get_balance(self):
        return self.balance

    def with_draw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return amount
        else:
            return f"Insufficient Balance"

ostad = Banking("Ostad", 10000)
print(f"Account name: {ostad.name}\nAccount Balance: {ostad.balance}\nDeposit Balance: {ostad.deposit(5000)}\nAfter deposit, Your Current Balance: {ostad.get_balance()}\nWithdraw Balance: {ostad.with_draw(1000)}\nAfter withdraw, Your Current Balance: {ostad.get_balance()}")
