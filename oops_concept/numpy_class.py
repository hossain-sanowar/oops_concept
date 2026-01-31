class Shape:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        pi=3.14
        return pi*self.radius**2


clsshape=Shape(10)
print(clsshape.area())