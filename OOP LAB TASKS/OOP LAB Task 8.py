class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")


class Staff(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def additional_info(self):
        print(f"Department: {self.department}")


FILE_NAME = "employee_details.txt"

def read_employees():
    """Reads employee information from the file."""
    employees = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, age, employee_id, position, department = line.strip().split(",")
                employees.append(Staff(name, int(age), employee_id, position, department))
    except FileNotFoundError:
        print("No employee records found. Starting fresh.")
    return employees

def add_employee(employees):
    """Adds a new employee."""
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    position = input("Enter Position: ")
    department = input("Enter Department: ")
    new_employee = Staff(name, age, employee_id, position, department)
    employees.append(new_employee)
    print("Employee added successfully!")

def save_employees(employees):
    """Saves employee information to the file."""
    with open(FILE_NAME, "w") as file:
        for emp in employees:
            file.write(f"{emp.name},{emp.age},{emp.employee_id},{emp.position},{emp.department}\n")
    print("Employee records saved to file.")

# Main program
def main():
    employees = read_employees()

    while True:
        print("\nEmployee Management System")
        print("1. Display All Employees")
        print("2. Add New Employee")
        print("3. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            if not employees:
                print("No employee records found.")
            else:
                for i, emp in enumerate(employees, start=1):
                    print(f"\nEmployee {i}:")
                    emp.display_info()
                    emp.additional_info()

        elif choice == "2":
            add_employee(employees)

        elif choice == "3":
            save_employees(employees)
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
