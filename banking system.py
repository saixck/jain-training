#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. Your new balance is ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Your new balance is ₹{self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Your current balance is ₹{self.balance}")


def main():
    accounts = {}  

    while True:
        print("\nChoose an option:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            
            account_number = int(input("Enter account number: "))
            accounts[account_number] = Account(account_number, balance=0)  
            print("Account created successfully!")

        elif choice == 2:
            account_number = int(input("Enter account number: "))
            if account_number in accounts:
                amount = int(input("Enter deposit amount: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.")
        elif choice == 3:
            account_number = int(input("Enter account number: "))
            if account_number in accounts:
                amount = int(input("Enter withdrawal amount: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")
        elif choice == 4:
            account_number = int(input("Enter account number: "))
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account not found.")
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




