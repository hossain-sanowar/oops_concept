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
        sum=self.num*(self.num+1)/2
        return sum

    def oneTohun(self,num):
        for i in range(num):
            if i%2==0:
                print(i)

series=newSeries(4)
print(series.numseries())
print(series.oneTohun(5))

class oddNumber(newSeries):
    def __init__(self, num):
        super().__init__(num)
        self.num=num

    def get_oddNumber(self):
        for i in range(1,self.num+1):
            if i%2!=0:
                print(i)


oddnum=oddNumber(5)
print(oddnum.get_oddNumber())

class highScore:
    def __init__(self, list):
        self.list = list
        self.score = 0

    def maxScore(self):
        return max(self.list)

    def minScore(self):
        return min(self.list)

    def indexing(self):
        return self.list.index(self.minScore())

    def numIndexing(self):
        return self.list[2]

    def add(self):
        return self.list[0]+self.list[1]



highscore=highScore([3,4,5,6,8])
print(highscore.maxScore())
print(highscore.minScore())
print(highscore.indexing())
print(highscore.numIndexing())
print(highscore.add())


class highScore2:
    def __init__(self, list):