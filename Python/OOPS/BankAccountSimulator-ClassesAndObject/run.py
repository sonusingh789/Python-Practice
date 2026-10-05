# Bank Account Simulator

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")

    def show_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance: ${self.balance}")


accounts = {}


def create_account():
    name = input("Enter account holder's name: ").strip()

    try:
        initial_deposit = float(input("Enter initial deposit amount: "))
        
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return

        account = BankAccount(name, initial_deposit)
        accounts[name] = account

        print("Account created successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def access_account():
    name = input("Enter your name: ").strip()

    if name in accounts:
        account = accounts[name]

        while True:
            print("\n--- Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Details")
            print("4. Check Balance")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid amount.")

            elif choice == "2":
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid amount.")

            elif choice == "3":
                account.show_details()

            elif choice == "4":
                account.check_balance()

            elif choice == "5":
                print("Exiting account menu.")
                break

            else:
                print("Invalid choice.")

    else:
        print("Account not found. Please create an account first.")


while True:
    print("\n--- Bank Account Simulator ---")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        create_account()

    elif choice == "2":
        access_account()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid input.")





    





    