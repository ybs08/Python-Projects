import json
class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.transactions = []
       
      

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Successfully withdrawn! Current balance: {self.account_balance}")
            self.transactions.append({"Transaction": f"{amount} was withdrawn."}) 
        else:
            print(f"Insufficient funds. Balance: {self.account_balance}") 
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Successfuly deposited! Current balance:{self.account_balance}")
        self.transactions.append({"Transaction": f"{amount} was deposited."})
    def get_balance(self):
        return self.account_balance
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.transactions, f)
    def load_from_file(self,filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.transactions = []
                for transaction in data:
                    self.transactions.append({"Transaction": transaction["Transaction"]})
        except FileNotFoundError:
            print("File not saved yet")

class SavingsAccount(BankAccount):
    def __init__(self, account_balance, withdrawal_limit=6):
        super().__init__(account_balance)
        self.withdrawal_limit = withdrawal_limit
        self.withdrawals_made = 0

    def withdraw(self, amount):
        if self.withdrawals_made >= self.withdrawal_limit:
            print("Withdrawal limit reached for this period.")
            return
        if amount <= self.account_balance:
            self.account_balance -= amount
            self.withdrawals_made += 1
            print(f"Successfully withdrawn! Current banlance: {self.account_balance}")
        else:
            print(f"Insuffiecient funds. Balance: {self.account_balance}")
class CheckingAccount(BankAccount):
    def __init__(self, account_balance, overdraft_limit=-500):
        super().__init__(account_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.account_balance - amount >= self.overdraft_limit:
            self.account_balance -= amount
            print(f"Successfully withdrawn. Current balance: {self.account_balance}")
        else:
            print(f"Insufficient funds. Balance: {self.account_balance}")


            


account = BankAccount(1000)
account.deposit(200)
account.withdraw(100)
account.save_to_file("transactions.json")

new_account = BankAccount(0)
new_account.load_from_file("transactions.json")
print(new_account.transactions)