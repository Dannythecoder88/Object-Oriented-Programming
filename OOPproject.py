class BankAccount:

    intrest_amt = 1.06

    def __init__(self, owner, act_num, balance):
        self.account_number= act_num
        self.owner= owner
        self.balance= balance
        self.trans_hist= []

    def get_balance(self):
        return "('{}': {})".format(self.owner, self.balance)


    def deposit(self, amount):
        if amount <= 0:
            print("Must deposit amount")
        else:
            self.balance += amount
        self.trans_hist.append ("Deposited: $" + str(amount))


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.trans_hist.append("Withdrew: $" + str(amount))

    def apply_intrest(self):
        self.balance = int(self.balance * self.intrest_amt)

class Account_Manager:
    def __init__(self):
        self.managed_accounts = []
        
    def add_account(self, act):
        if act not in self.managed_accounts:
            self.managed_accounts.append(act)

    def remove_account(self, act):
        if act in self.managed_accounts:
            self.managed_accounts.remove(act)

    def print_acts(self):
        for act in self.managed_accounts:
            print('-->', act.owner)


manager = Account_Manager()

act_1 = BankAccount("Daniel Joseph", "001", 2000)
act_2 = BankAccount("Charles Joseph", "002", 1500)



manager.add_account(act_1)
manager.add_account(act_2)

manager.remove_account(act_2)
manager.print_acts()

# act_1.apply_intrest()

# print(act_1.get_balance())






# act_1.deposit(300)
# act_1.withdraw(2006)
# print(act_1.get_balance())
# print(act_1.trans_hist)