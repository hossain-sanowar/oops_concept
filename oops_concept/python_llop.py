class Loop:
    def __init__(self,data):
        self.data = data

    def iterate(self):
        for i in self.data:
            yield i

    def total(self):
        return sum(self.data())

clsLoop=Loop(data=[1,2,3,4,5])
iterate_data=clsLoop.iterate()
print(list(iterate_data))
