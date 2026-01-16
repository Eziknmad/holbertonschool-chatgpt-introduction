#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")


def main():
    print("Starting checkbook program...")
    cb = Checkbook()
    prompt = "What would you like to do? (deposit, withdraw, balance, exit): "
    while True:
        action = input(prompt).lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                continue
            cb.deposit(amount)
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                continue
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
