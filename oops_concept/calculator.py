from abc import ABC, abstractmethod
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b


cal=Calculator(2,3)
print(cal.a)
print(cal.b)
print(cal.add())
print(cal.sub())
print(cal.mul())
