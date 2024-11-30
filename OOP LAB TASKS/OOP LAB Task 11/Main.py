from manager import Manager
from worker import Worker
from file_handler import FileHandler

def add_employee(employees):
    """Add a new employee"""
    employee_type = input("Enter employee type (manager/worker): ").strip().lower()
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = int(input("Enter salary: "))
    
    if employee_type == 'manager':
        department = input("Enter department: ")
        employees.append(Manager(name, age, salary, department))
    elif employee_type == 'worker':
        hours_worked = int(input("Enter hours worked: "))
        employees.append(Worker(name, age, salary, hours_worked))
    else:
        print("Invalid employee type!")

def display_employees(employees):
    """Display all employees"""
    for employee in employees:
        employee.display_info()
        print('-' * 20)

def update_employee(employees):
    """Update an employee's information"""
    name = input("Enter name of employee to update: ")
    for employee in employees:
        if employee.get_name() == name:
            attribute = input("Enter attribute to update (name/age/salary/department/hours_worked): ").strip().lower()
            if attribute == 'name':
                employee.set_name(input("Enter new name: "))
            elif attribute == 'age':
                employee.set_age(int(input("Enter new age: ")))
            elif attribute == 'salary':
                employee.set_salary(int(input("Enter new salary: ")))
            elif attribute == 'department' and isinstance(employee, Manager):
                employee.set_department(input("Enter new department: "))
            elif attribute == 'hours_worked' and isinstance(employee, Worker):
                employee.set_hours_worked(int(input("Enter new hours worked: ")))
            break

def delete_employee(employees):
    """Delete an employee"""
    name = input("Enter name of employee to delete: ")
    for i, employee in enumerate(employees):
        if employee.get_name() == name:
            del employees[i]
            break

def main():
    """Main program loop"""
    filename = 'employees.csv'
    employees = FileHandler.load_employees(filename)

    while True:
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save and Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_employee(employees)
        elif choice == 2:
            display_employees(employees)
        elif choice == 3:
            update_employee(employees)
        elif choice == 4:
            delete_employee(employees)
        elif choice == 5:
            FileHandler.save_employees(employees, filename)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
