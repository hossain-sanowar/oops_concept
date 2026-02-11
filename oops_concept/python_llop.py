class Loop:
    def __init__(self,data):
        self.data = data

    def iterate(self):
        for i in self.data:
            yield i

    def total(self,a):
        return sum(a)

clsLoop=Loop(data=[1,2,3,4,5])
iterate_data=clsLoop.iterate()
print(list(iterate_data))

print(clsLoop.total([1,2,3,4,5]))
