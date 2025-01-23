class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be greater than 0.")

    def check_balance(self):
        """Check the current balance."""
        print(f"Current balance: ${self.balance}")


def main():
    print("Welcome to the Bank!")
    name = input("Enter account holder name: ")
    account = BankAccount(name)
    
    while True:
        print("\nSelect an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        option = input("Enter option (1/2/3/4): ")

        if option == "1":
            amount = float(input("Enter deposit amount: $"))
            account.deposit(amount)
        elif option == "2":
            amount = float(input("Enter withdrawal amount: $"))
            account.withdraw(amount)
        elif option == "3":
            account.check_balance()
        elif option == "4":
            print("Exiting the bank system. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":     # This conditional block checks whether the Python file is being run directly or being imported as a module. special construct in Python, it is used to run code only when the script is executed directly.
    main()
