from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self, radius):
        return 3.14*radius**2

circle=Circle()
print(circle.area(10))


class Rectangle(Shape):
    def area(self, height, width):
        return height*width
