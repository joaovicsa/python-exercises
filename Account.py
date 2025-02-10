class Account:
    def __init__(self, name, balance):
        self.name = name
        if balance>0:
            self.balance = balance
        else:
            self.balance = 0.00

    def deposit(self, depositAmount):
        if depositAmount > 0.00:
            self.balance += depositAmount

    # Implements withdraw
    def withdraw(self, withdrawAmount):
        if withdrawAmount <= self.balance:
            self.balance -= withdrawAmount

account1 = Account(name="Jane Green", balance=64.00)
account2 = Account(name="John Blue", balance=-6.00)

print(account1.name + " balance: " + str(account1.balance))
print(account2.name + " balance: " + str(account2.balance))

depositAmount = float(input("Enter the amount to be deposited in " + account1.name + " account: "))
if depositAmount < 0.00:
    print("Value invalid!")
else:
    print("Adding " + str(depositAmount) + " to account balance.")
    account1.deposit(depositAmount)

print(account1.name + " balance: " + str(account1.balance))
print(account2.name + " balance: " + str(account2.balance))

depositAmount = float(input("Enter the amount to be deposited in " + account2.name + " account: "))
if depositAmount < 0.00:
    print("Value invalid!")
else:
    print("Adding " + str(depositAmount) + " to account balance.")
    account2.deposit(depositAmount)

print(account1.name + " balance: " + str(account1.balance))
print(account2.name + " balance: " + str(account2.balance))

withdrawAmount = float(input("Enter the amount to be withdrawn in " + account1.name + " account: "))
if withdrawAmount > account1.balance:
    print("Withdraw value exceeded account balance.")
else:
    account1.withdraw(withdrawAmount)
    print("Removing " + str(withdrawAmount) + " from account balance.")

print(account1.name + " balance: " + str(account1.balance))
print(account2.name + " balance: " + str(account2.balance))
