class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def additional_info(self):
        print(f"Number of doors: {self.num_doors}")
class LuxuryCar(Car):
    def __init__(self, make, model, num_doors, features):
        super().__init__(make, model, num_doors)
        self.features = features

    def additional_info(self):
        super().additional_info()
        print(f"Luxury Features: {self.features}")
luxury_car = LuxuryCar("Mercedes", "S-Class", 4, ["Leather seats", "Premium sound system", "Sunroof"])
luxury_car.display_info()
luxury_car.additional_info()
