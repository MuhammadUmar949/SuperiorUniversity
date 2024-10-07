class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}")

class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department

    def additional_info(self):
        print(f"Department: {self.department}")

class Worker(Employee):
    def __init__(self, name, position, hours_worked):
        super().__init__(name, position)
        self.hours_worked = hours_worked

    def additional_info(self):
        print(f"Hours Worked: {self.hours_worked}")

manager = Manager("Alice", "Manager", "IT")
worker = Worker("Bob", "Worker", 40)

manager.display_info()
manager.additional_info()
worker.display_info()
worker.additional_info()
