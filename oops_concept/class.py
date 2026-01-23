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



cls=Calculator(34,5)
print(cls.add())
print(cls.sub())
print(cls.mul())