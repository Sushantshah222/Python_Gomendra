class BankAccount:
    def __init__(self, ac_holder_name, acc_number, passkey, balance=0,):
        self.ac_holder_name = ac_holder_name
        self.acc_number = acc_number
        self.balance = balance
        self.passkey = passkey

    def withdraw(self):
        withdraw_amt = int(input("Enter the amount you wanna withdraw: "))

        passkey = input("Passkey: ")
        if passkey != self.passkey:
            print("Unauthorized user...")
            return

        self.show_balance()

        if (0 < withdraw_amt < self.balance):
            print("Withdrawing krr......")
            self.balance -= withdraw_amt
            print(f"Amount Rs: {withdraw_amt} withdrawn successfully")

        else:
            print("Garib ho vai app")

        self.show_balance()

    def deposit(self):
        deposit_amt = int(input("Enter the amount you wanna deposit: "))

        if (0 < deposit_amt):
            self.balance += deposit_amt
            print(f"Amount Rs: {deposit_amt} Deposited successfully")
            self.show_balance()
        else:
            print("Garib ho vai app")

    def show_balance(self):
        print(f"You have Rs {self.balance} in your account")

    def display_info(self):
        print(f"Account Holder Name: {self.ac_holder_name}")
        print(f"Account Holder Number: {self.acc_number}")
        self.show_balance()


class Bank:
    accountholders = {
            "ac_holder_name": [],
            "ac_holder_num": [],
            "ac_instance": []
        }
    
    initial_deposit=0
    acc_num = 0

    def __init__(self) -> None:
        pass
    
    def create_account(self):
        ac_holder_name = input("Enter account holder name: ")
        passkey = input("Create a passkey: ")
        self.initial_deposit = int(input("Enter the initial deposit amount: "))

        newBankAc = BankAccount(ac_holder_name, self.acc_num, passkey, self.initial_deposit)

        self.accountholders["ac_holder_name"].append(ac_holder_name)
        self.accountholders["ac_holder_num"].append(self.acc_num)
        self.accountholders["ac_instance"].append(newBankAc)

        self.acc_num+=1
        print("Account Created Successfully")
        return newBankAc
    
    def find_account(self):
        choice = input("Find by Ac.Name (name) or Ac.Number (num): ")

        index = -1

        if choice == "name":
            name = input("Enter the Account Name of user: ")
            for idx, ac_name in enumerate(self.accountholders["ac_holder_name"]):
                if name == ac_name:
                    index = idx
                    break

        else:
            num = int(input("Enter the Account Number of user: "))
            for idx, ac_num in enumerate(self.accountholders["ac_holder_num"]):
                if num == ac_num:
                    index = idx
                    break

        if index !=-1:
            print("User Exists...")
        return index
    
    def display_info(self):
        index = self.find_account()
                   
        if (index == -1):
            print("The Account Wasn't found")
            return
        
        print("Detail of the account: ")
        self.accountholders["ac_instance"][index].display_info()


bankInstance = Bank()

bank_ac_instance = bankInstance.create_account()
# bankInstance.find_account()
# bankInstance.display_info()

bank_ac_instance.deposit()
bank_ac_instance.withdraw()
