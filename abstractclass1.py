from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    def get_color(self):
        return self.color

class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):

    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating objects
circle = Circle("red", 5)
print("Circle area:", circle.area())
print("Circle color:", circle.get_color())

rectangle = Rectangle("blue", 4, 6)
print("Rectangle area:", rectangle.area())
print("Rectangle color:", rectangle.get_color())