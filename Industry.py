import random
import Account
import Employee

class Industry:
    def __init__(self):
        self.employees = []

    def menu():
        print("--------------##-------------------")
        print("Select an option: ")
        print("1. Create new Employee")
        print("2. Search Employee")
        print("3. Delete Employee")
        print("4. List all active Employees")
        print("5. Check Salary Rank")
        print("--------------##-------------------")
        return int(input("Type a number accordingly: "))

    def newEmployee(self, employee):
        self.employees.append(employee)

    def searchEmployee(self, employees):
        word = input("Type a name or a role to search: ")
        for x in employees:
            if employees[x].name == word or employees[x].role == word:
                print(employees[x])

        found = employees.index(word) if word in employees else -1
        if found == -1:
            print("Couldn't find an Employee.")

    def removeEmployee(self, index):
        self.employees.remove(index)

# Generate a list of 20 Employee objects
employee_list = []
roles = ["Manager", "Developer", "Designer", "Analyst", "Intern"]
names = [
    "Alice Smith", "Bob Johnson", "Charlie Brown", "Diana Prince", "Ethan Hunt",
    "Fiona Apple", "George Miller", "Hannah Baker", "Ian Curtis", "Julia Roberts",
    "Kevin Bacon", "Laura Palmer", "Mike Ross", "Nancy Drew", "Oscar Wilde",
    "Pam Beesly", "Quinn Fabray", "Rachel Green", "Steve Jobs", "Tina Fey"
]

for i in range(20):
    name = names[i]
    role = random.choice(roles)
    salary = random.randint(30000, 120000)  # Random salary between 30k and 120k
    account = Account(name=f"{name}'s Account", balance=random.randint(1000, 20000))
    employee = Employee(name=name, role=role, account=account, salary=salary)
    employee_list.append(employee)

