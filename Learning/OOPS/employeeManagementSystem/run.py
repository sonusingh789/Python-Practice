class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print("\n--- Employee Details ---")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")

    def calculate_bonus(self):
        return self.salary * 0.10


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

    def calculate_bonus(self):
        return super().calculate_bonus() * 2


class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def calculate_bonus(self):
        return self.salary * 0.05


employees = []


def add_employee():
    print("\n--- Choose Employee Type ---")
    print("1. Regular Employee")
    print("2. Manager")
    print("3. Developer")

    choice = int(input("Enter choice: ").strip())

    name = input("Enter Employee Name: ").strip()
    emp_id = input("Enter Employee ID: ").strip()
    salary = float(input("Enter Employee Salary: ").strip())

    if choice == 1:
        employees.append(Employee(name, emp_id, salary))

    elif choice == 2:
        department = input("Enter Department: ").strip()
        employees.append(
            Manager(name, emp_id, salary, department)
        )

    elif choice == 3:
        programming_language = input(
            "Enter Programming Language: "
        ).strip()

        employees.append(
            Developer(
                name,
                emp_id,
                salary,
                programming_language
            )
        )

    else:
        print("Invalid Choice")


def display_all_employees():
    print("\n--- All Employees ---")

    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        employee.display_info()
        print(f"Bonus: {employee.calculate_bonus()}")
        print("-" * 30)


while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Exit")

    choice = int(input("Enter your choice (1-3): ").strip())

    if choice == 1:
        add_employee()

    elif choice == 2:
        display_all_employees()

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")