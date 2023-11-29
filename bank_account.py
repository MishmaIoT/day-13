class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def deposit(self, amount):
        self.account.balance += amount
        print(f"{self.name} deposited ${amount} into account {self.account.account_number}.")

    def withdraw(self, amount):
        if amount <= self.account.balance:
            self.account.balance -= amount
            print(f"{self.name} withdrew ${amount} from account {self.account.account_number}.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Balance for {self.name} ({self.account.account_number}): ${self.account.balance}")

# Example usage:
account1 = Account("12345")
customer1 = Customer("Bob", account1)
customer1.deposit(1000)
customer1.withdraw(500)
customer1.check_balance()
