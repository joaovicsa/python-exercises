class Account:
    def __init__(self, name, balance):
        self.name = name
        if balance>0:
            self.balance = balance
        else:
            self.balance = 0.00

    def deposit(self, depositAmount):
        if self.balance > 0.00:
            self.balance += depositAmount

    # Implements withdraw

account1 = Account(name="Jane Green", balance=64.00)
account2 = Account(name="John Blue", balance=-6.00)

print(account1.name + " balance: " + str(account1.balance))
print(account2.name + " balance: " + str(account2.balance))

depositAmount = float(input("Enter the amount to be deposited in " + account1.name + " account: "))
account1.deposit(depositAmount)
print("Adding " + str(depositAmount) + " to account balance.")

print(account1.name + " balance: " + str(account1.balance))
print(account2.name + " balance: " + str(account2.balance))

depositAmount = float(input("Enter the amount to be deposited in " + account2.name + " account: "))
account2.deposit(depositAmount)
print("Adding " + str(depositAmount) + " to account balance.")