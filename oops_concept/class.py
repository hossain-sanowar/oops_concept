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

    def age(self):
        add, sub, mul, div, pow = self.numseries()
        return add, sub, mul, div, pow

    def count(self,num):
        add = self.add()
        return add+num


newclas=newCalculator(34,5)
print(newclas.add())
print(newclas.numseries())
print(newclas.age())
print(newclas.count(34))


class newSeries:
    def __init__(self, num):
        self.num = num
    def numseries(self):
        sum=0
        for num in self.num:
            sum=self.num*(self.num+1)/2
        return sum


