import os

class BankAccount:
    def __init__(self, AccNumber, Accholder_name, balance=0):
        self.AccNumber = AccNumber
        self.Accholder_name = Accholder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'Deposited {amount}. New balance: {self.balance}'
        else:
            return 'Invalid deposit amount.'
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f'Withdrew {amount}. New balance: {self.balance}'
        else:
            return 'Invalid withdrawal amount or insufficient balance.'
    
    def display_info(self):
        return f'Account Number: {self.AccNumber}, Account Holder Name: {self.Accholder_name}, Balance: {self.balance}'


class Bank:
    def __init__(self, filename='accounts.txt'):
        self.accounts = []
        self.filename = filename
        self.load_accounts()
    
    def load_accounts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    AccNumber, Accholder_name, balance = line.strip().split(',')
                    account = BankAccount(AccNumber, Accholder_name, float(balance))
                    self.accounts.append(account)
    
    def save_accounts(self):
        with open(self.filename, 'w') as file:
            for account in self.accounts:
                file.write(f'{account.AccNumber},{account.Accholder_name},{account.balance}\n')
    
    def create_account(self, AccNumber, Accholder_name, starting_bal=0):
        account = BankAccount(AccNumber, Accholder_name, starting_bal)
        self.accounts.append(account)
        self.save_accounts()
        return f'Account created successfully. Account Number: {account.AccNumber}, Account Holder Name: {account.Accholder_name}, Balance: {account.balance}'
    
    def find_account(self, AccNumber):
        for account in self.accounts:
            if account.AccNumber == AccNumber:
                return account
        return None
    
    def display_account(self, AccNumber):
        account = self.find_account(AccNumber)
        if account:
            return account.display_info()
        else:
            return 'Account not found.'
    
    def deposit(self, AccNumber, amount):
        account = self.find_account(AccNumber)
        if account:
            result = account.deposit(amount)
            self.save_accounts()
            return result
        else:
            return 'Account not found.'
    
    def withdraw(self, AccNumber, amount):
        account = self.find_account(AccNumber)
        if account:
            result = account.withdraw(amount)
            self.save_accounts()
            return result
        else:
            return 'Account not found.'

def main():
    bank = Bank()
    
    while True:
        print("\n1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            AccNumber = input("Enter account Number: ")
            Accholder_name = input("Enter Account Holder Name: ")
            starting_bal = float(input("Enter Initial Balance: "))
            print(bank.create_account(AccNumber, Accholder_name, starting_bal))
        
        elif choice == '2':
            AccNumber = input("Enter account Number: ")
            print(bank.display_account(AccNumber))
        
        elif choice == '3':
            AccNumber = input("Enter account Number: ")
            amount = float(input("Enter amount to deposit: "))
            print(bank.deposit(AccNumber, amount))
        
        elif choice == '4':
            AccNumber = input("Enter account Number: ")
            amount = float(input("Enter amount to witdraw: "))
            print(bank.withdraw(AccNumber, amount))
        
        elif choice == '5':
            print("Exiting the banking system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
