import sqlite3
import os
import uuid

from myQueries import myQueries, BANK_ACCOUNT_TABLE_NAME, BANK_TABLE_NAME

def clear_screen():
    print('\033[2J\033[1;1H')

class BankAccount:
    def __init__(self, ac_holder_name, acc_number, passkey, balance=0) -> None:
        try:
            self.acc_number = acc_number

            # Hamro Naya Bank Khata ko sucharu
            db_cursor.execute(
                myQueries["bank_ac"]["ac_create"],
                (self.acc_number, ac_holder_name, passkey, balance)
            )
            db_connection.commit()
            print("Bank account created successfully !!!")

        except sqlite3.OperationalError as err:
            print(err)

    def withdraw(self):
        withdraw_amt = int(input("Enter the amount you wanna withdraw: "))
        passkey = input("Passkey: ")
        # getting passkey fro, database
        res = db_cursor.execute(myQueries["bank_ac"]["withdraw_details"], (self.acc_number,) )
        user_passkey, user_balance = res.fetchone() # not hashed

        if passkey != user_passkey:
            print("Unauthorized user...")
            return

        print(f"you have Rs{user_balance} in you bank account")
        print('\n')

        if 0 < withdraw_amt < user_balance:
            user_balance -= withdraw_amt

            db_cursor.execute(myQueries["bank_ac"]["update_balance"], (user_balance, self.acc_number))
            db_connection.commit()

            print("Withdrawing krr......")
            print(f"Amount Rs: {withdraw_amt} withdrawn successfully")

        else:
            print("Garib ho vai app")

        self.show_balance()

    def deposit(self):
        prev_balance = self.show_balance()
        deposit_amt = int(input("Enter the amount you wanna deposit: "))

        if 0 < deposit_amt:
            newBalance = prev_balance + deposit_amt

            try:
                db_cursor.execute(myQueries["bank_ac"]["update_balance"], (newBalance, self.acc_number))
                db_connection.commit()

                print(f"Amount Rs: {deposit_amt} Deposited successfully")

            except sqlite3.OperationalError as err:
                print(err)

            self.show_balance()
        else:
            print("Garib ho vai app")

    def show_balance(self) -> int:
        try:
            res = db_cursor.execute(myQueries["bank_ac"]["get_balance"], (self.acc_number,))
            balance = res.fetchone()
            print(f"You have Rs {balance[0]} in your account")
            return balance[0]

        except sqlite3.OperationalError as err:
            print(err)

    def display_info(self):
        try:
            res = db_cursor.execute(myQueries['bank_ac']['get_info'], (self.acc_number,))
            data = res.fetchone()
            print(data)

        except sqlite3.OperationalError as err:
            print(err)

class Bank:
    def __init__(self) -> None:
        pass

    def create_account(self):
        ac_holder_name = input("Enter account holder name: ")
        passkey = input("Create a passkey: ")
        initial_deposit = int(input("Enter the initial deposit amount: "))

        ac_holder_num = str(uuid.uuid4())

        try:
            newBankAc = BankAccount(
                ac_holder_name, ac_holder_num, passkey, initial_deposit
            )

            db_cursor.execute(
                myQueries["bank"]["ac_create"], (ac_holder_num, ac_holder_name)
            )
            db_connection.commit()
            print("Bank account linked to bank successfully !!!")

            return newBankAc

        except sqlite3.OperationalError as err:
            print(err)

    def find_account(self):
        choice = input("Find by Ac.Name (name) or Ac.Number (num): ")

        db_user_ac_num = ""

        if choice == "name":
            ac_name = input("Enter the Account Name of user: ")
            response = db_cursor.execute(
                myQueries["bank"]["find_by_ac_name"], (ac_name,)
            )
            db_user_ac_num = response.fetchone()

        elif choice == "num":
            ac_num = input("Enter the Account Number of user: ")
            response = db_cursor.execute(myQueries["bank"]["find_by_ac_num"], (ac_num,))
            db_user_ac_num = response.fetchone()

        else:
            print("God Damm stupids !!!")
            return

        if db_user_ac_num:
            print("User Exists...")

        return db_user_ac_num[0]

    def display_info(self):
        db_user_ac_num = self.find_account()

        if not db_user_ac_num:
            print("The Account Wasn't found")
            return

        print("\nDetail of the account: ")
        res = db_cursor.execute(myQueries["bank"]["get_user"], (db_user_ac_num,))
        user_ac_num, user_name = res.fetchone()
        print(f"User Account Number: {user_ac_num}\nUser Account Name: {user_name}")


if __name__ == "__main__":
    dbName = os.getenv("BANKING_DB_NAME", "Paisa.db")
    db_connection = sqlite3.connect(dbName)
    db_cursor = db_connection.cursor()

    # not gonna hash the passkey though
    db_cursor.execute(myQueries["bank_ac"]["create_table"])
    
    db_cursor.execute(myQueries["bank"]["create_table"])

    #
    bankInstance = Bank()

    bank_ac_instance = bankInstance.create_account()
    _  = input("Enter any key to continue...")
    clear_screen()

    bankInstance.find_account()
    _  = input("Enter any key to continue...")
    clear_screen()

    bankInstance.display_info()
    _  = input("Enter any key to continue...")
    clear_screen()

    bank_ac_instance.deposit()
    _  = input("Enter any key to continue...")
    clear_screen()
    
    bank_ac_instance.withdraw()