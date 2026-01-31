class Shape:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        pi=3.14
        return pi*self.radius**2

    def perimeter(self):
        pi=3.14
        return 2*pi*self.radius

    def rectangle(self,length, width):
        area=length*width
        return area

    def rectangle_primeter(self):
        length=self.rectangle()
        width=self.perimeter()
        return 2*(length+width)




clsshape=Shape(10)
print(clsshape.area())
print(clsshape.perimeter())
print(clsshape.rectangle(10,20))
