class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"


person1 = Person("Umar", 20)

print(person1.name)  
print(person1.age)   
print(person1)  
