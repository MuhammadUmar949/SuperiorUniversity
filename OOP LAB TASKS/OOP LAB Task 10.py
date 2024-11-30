import csv
class Employee:
    def __init__(self, name, age, salary):
        self.__name = name       
        self.__age = age         
        self.__salary = salary   

    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Salary: {self.__salary}")


class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.__department = department 

    
    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.__department}")


class Worker(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.__hours_worked = hours_worked  

    
    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

    def display_info(self):
        super().display_info()
        print(f"Hours Worked: {self.__hours_worked}")


FILE_NAME = "employee_data.csv"

def load_employees():
    """Load employees from CSV file"""
    employees = []
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "Manager":
                    employees.append(Manager(row[1], int(row[2]), float(row[3]), row[4]))
                elif row[0] == "Worker":
                    employees.append(Worker(row[1], int(row[2]), float(row[3]), int(row[4])))
    except FileNotFoundError:
        print("No previous employee data found.")
    return employees

def save_employees(employees):
    """Save employee data to CSV file"""
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for emp in employees:
            if isinstance(emp, Manager):
                writer.writerow(["Manager", emp.get_name(), emp.get_age(), emp.get_salary(), emp.get_department()])
            elif isinstance(emp, Worker):
                writer.writerow(["Worker", emp.get_name(), emp.get_age(), emp.get_salary(), emp.get_hours_worked()])
    print("Employee data saved successfully.")

def add_employee(employees):
    """Add a new employee"""
    print("Enter Employee Details:")
    name = input("Name: ")
    age = int(input("Age: "))
    salary = float(input("Salary: "))
    emp_type = input("Enter Employee Type (Manager/Worker): ")

    if emp_type.lower() == "manager":
        department = input("Department: ")
        employee = Manager(name, age, salary, department)
    elif emp_type.lower() == "worker":
        hours_worked = int(input("Hours Worked: "))
        employee = Worker(name, age, salary, hours_worked)
    else:
        print("Invalid employee type.")
        return

    employees.append(employee)
    print(f"{emp_type.capitalize()} added successfully.")

def update_employee(employees):
    """Update employee information"""
    name = input("Enter the name of the employee to update: ")
    for emp in employees:
        if emp.get_name().lower() == name.lower():
            print("Select what to update:")
            print("1. Name")
            print("2. Age")
            print("3. Salary")
            print("4. Department (Manager Only)")
            print("5. Hours Worked (Worker Only)")
            choice = input("Enter choice: ")
            if choice == "1":
                new_name = input("Enter new name: ")
                emp.set_name(new_name)
            elif choice == "2":
                new_age = int(input("Enter new age: "))
                emp.set_age(new_age)
            elif choice == "3":
                new_salary = float(input("Enter new salary: "))
                emp.set_salary(new_salary)
            elif choice == "4" and isinstance(emp, Manager):
                new_dept = input("Enter new department: ")
                emp.set_department(new_dept)
            elif choice == "5" and isinstance(emp, Worker):
                new_hours = int(input("Enter new hours worked: "))
                emp.set_hours_worked(new_hours)
            else:
                print("Invalid choice or option not applicable.")
            print("Employee updated successfully.")
            return
    print("Employee not found.")

def delete_employee(employees):
    """Delete an employee"""
    name = input("Enter the name of the employee to delete: ")
    for emp in employees:
        if emp.get_name().lower() == name.lower():
            employees.remove(emp)
            print("Employee deleted successfully.")
            return
    print("Employee not found.")

def display_all_employees(employees):
    """Display all employee information"""
    if not employees:
        print("No employees available.")
        return
    for emp in employees:
        emp.display_info()
        print("-" * 30)


def main():
    employees = load_employees()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Display All Employees")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            update_employee(employees)
        elif choice == "3":
            delete_employee(employees)
        elif choice == "4":
            display_all_employees(employees)
        elif choice == "5":
            save_employees(employees)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
