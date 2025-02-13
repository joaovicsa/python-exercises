import random
from Account import Account
from Employee import Employee

class Industry:
    def __init__(self):
        self.employees = []

    @staticmethod
    def menu():
        print("--------------##-------------------")
        print("Select an option: ")
        print("1. Create new Employee")
        print("2. Search Employee")
        print("3. Delete Employee")
        print("4. List all active Employees")
        print("5. Check Salary Rank")
        print("0. Exit")
        print("--------------##-------------------")
        return int(input("Type a number accordingly: "))

    def new_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully!")

    def search_employee(self):
        word = input("Type a name or a role to search: ")
        found = [e for e in self.employees if word.lower() in e.name.lower() or word.lower() in e.name.lower() or word.lower() in e.role.lower()]
        if found:
            for emp in found:
                emp.displayEmployee()
        else:
            print("Couldn't find an Employee.")

    def remove_employee(self):
        name = input("Enter the Employee name to delete: ")
        for e in self.employees:
            if e.name.lower() == name.lower():
                self.employees.remove(e)
                print(f"Employee {name} removed successfully!")
                return
            print("Employee not found!")

    def list_employee(self):
        if not self.employees:
            print("No employees found.")
        else:
            for emp in self.employees:
                emp.displayEmployee()

    def salary_rank(self):
        if not self.employees:
            print("No employees found.")
            return
        ranked = sorted(self.employees, key=lambda x: x.salary, reverse=True)
        print("Employees ranked by salary:")
        for emp in ranked:
            print(f"{emp.name}: ${emp.salary}")




industry = Industry()

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
    account = Account(name=name, balance=random.randint(1000, 20000))
    employee = Employee(name=name, role=role, account=account, salary=salary)
    industry.new_employee(employee)

while True:
    option = industry.menu()

    if option == 0:
        print("Exiting the program.")
        break
    elif option == 1:
        name = input("Enter the candidate's name: ")
        role = input("Enter the candidate's role: ")
        salary = random.randint(30000, 120000)
        account = Account(name = name, balance=0.00)
        candidate = Employee(name=name, role=role, account=account, salary=salary)
        industry.new_employee(candidate)
    elif option == 2:
        industry.search_employee()
    elif option == 3:
        industry.remove_employee()
    elif option == 4:
        industry.list_employee()
    elif option == 5:
        industry.salary_rank()
    else:
        print("Invalid Option. Try again!")