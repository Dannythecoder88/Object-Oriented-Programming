class BankAccount:


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

act_1 = BankAccount("Daniel Joseph", "001", 2000)

act_1.deposit(300)
act_1.withdraw(2006)
print(act_1.get_balance())
print(act_1.trans_hist)