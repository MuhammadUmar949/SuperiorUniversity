class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle: {self.width} x {self.height}"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

rectangle = Rectangle(width, height)

print(rectangle)
print(f"Area of the rectangle: {rectangle.area()}")
print(f"Perimeter of the rectangle: {rectangle.perimeter()}")
