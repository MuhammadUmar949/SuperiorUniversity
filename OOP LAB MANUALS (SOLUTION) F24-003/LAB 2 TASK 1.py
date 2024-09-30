# Define a class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


car1 = Car("Toyota", "Corolla", 2020)  
car2 = Car("Honda", "Civic", 2019)     


print(car1.brand)  
print(car2.model)  
