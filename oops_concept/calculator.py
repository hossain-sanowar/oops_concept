from abc import ABC, abstractmethod
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

cal=Calculator(2,3)
print(cal.a)
print(cal.b)

