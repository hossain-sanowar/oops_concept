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

    def div(self):
        return self.a / self.b

    def pow(self):
        return self.a ** self.b



cls=Calculator(34,5)
print(cls.add())
print(cls.sub())
print(cls.mul())
print(cls.div())
print(cls.pow())

class newCalculator(Calculator):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.a = a
        self.b = b
    def numseries(self):
        add = self.add()
        sub = self.sub()
        mul = self.mul()
        div = self.div()
        pow = self.pow()
        return add, sub, mul, div, pow


newclas=newCalculator(34,5)
print(newclas.add())
print(newclas.numseries())
