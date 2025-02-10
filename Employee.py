from Account import account1, account2

class Employee:
    def __init__(self, name, role, account, salary):
        self.name = name
        self.role = role
        self.salary = salary
        self.account = account

    def displayEmployee(self):
        print("Info about " + self.name)
        print("Salary: $" + str(self.salary))
        print("Role: " + self.role)

    def calculate_payment(self, months):
        print("Value received in " + str(months) + ": $" + str(self.salary * months))
        return self.salary * months


employee1 = Employee(account1.name, "Manufacturer", account1, 2700.00)
employee2 = Employee(account2.name, "Manager", account2, 6700.00)

employee1.displayEmployee()
employee2.displayEmployee()

months = int(input("How many months did " + employee1.name + " worked?"))
received = employee1.calculate_payment(months)
print("Adding $"+ str(received) + " to " + employee1.name + " account.")
employee1.account.deposit(received)
employee1.account.displayAccount()

months = int(input("How many months did " + employee2.name + " worked?"))
received = employee2.calculate_payment(months)
print("Adding $"+ str(received) + " to " + employee2.name + " account.")
employee2.account.deposit(received)
employee2.account.displayAccount()


