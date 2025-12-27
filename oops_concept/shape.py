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

    def perimeter(self, height, width):
        return 2*(height+width)

class Triangle(Shape):
    def area(self, height, width):
        return height*width/2
    def perimeter(self, height, width):
        return height*width/3

class CircleShape(Shape):
    def area(self, radius):
        return 3.14*radius**2



rectangle=Rectangle()
print(rectangle.area(10,10))
print(rectangle.perimeter(10,10))

triangle=Triangle()
print(triangle.area(10,10))
print(triangle.perimeter(10,10))