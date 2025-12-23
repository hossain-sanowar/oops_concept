from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self, radius):
        return 3.14*radius**2

    def perimeter(self, radius):
        return 3.14*2*radius

circle=Circle()
print(circle.area(10))
print(circle.perimeter(10))


class Rectangle(Shape):
    def area(self, height, width):
        return height*width

rectangle=Rectangle()
print(rectangle.area(10,10))
