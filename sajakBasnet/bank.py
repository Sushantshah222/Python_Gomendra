class BankAccount:
    def __init__(self, account_holder_name, ac_number, balance=0):
        self.account_holder_name = account_holder_name
        self.ac_number = ac_number
        self.balance = balance

    def withdraw(self, withdraw_amt):
        if withdraw_amt > self.balance:
            print("Your are Brokeee .")
        else:
            self.balance -= withdraw_amt
            print(f"Withdrawn amount: {withdraw_amt}")
            print(f"Remaining balance: {self.balance}")

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount
            print(f"\n{deposit_amount} has been deposited into your account")
            print(f"Your current balance is: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def display_info(self):
        print("----------------")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.ac_number}")
        print(f"Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        print("Creating Account...\n")
        name = input("Enter Account Holder Name: ")
        initial_deposit = int(input("Enter Initial Deposit amount: "))
        ac_number = len(self.accounts) + 1  # Simplistic account number generation
        new_account = BankAccount(name, ac_number, initial_deposit)
        self.accounts.append(new_account)
        print("Account created successfully!")

    def find_account(self, name):
        for account in self.accounts:
            if account.account_holder_name == name:
                return account
        return None

    def display_all_accounts(self):
        for account in self.accounts:
            account.display_info()


if __name__ == "__main__":
    bank = Bank()

    bank.create_account()

    print("\nAll accounts:")
    bank.display_all_accounts()

    print("\nFinding an account:")
    search_name = input("Enter search name: ")
    account = bank.find_account(search_name)
    if account:
        account.display_info()
    else:
        print("Account not found.")

    print("\nDisplaying all accounts again:")
    bank.display_all_accounts()
