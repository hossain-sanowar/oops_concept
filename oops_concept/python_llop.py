class Loop:
    def __init__(self,data):
        self.data = data

    def iterate(self):
        for i in self.data:
            yield i

    def total(self,a):
        return sum(a)

    def even(self,a):
        even_data=[]
        for i in a:
            if i % 2 == 0:
                even_data.append(i)
        return even_data

    def calc(self,a):
        Total=sum(a)
        Length=len(a)
        return Total, Length

    def add(self,a):
        total=sum(a)
        return total





clsLoop=Loop(data=[1,2,3,4,5])
iterate_data=clsLoop.iterate()
print(list(iterate_data))

print(clsLoop.total([1,2,3,4,5]))
print(clsLoop.even([1,2,3,4,5]))
print(clsLoop.calc([1,2,3,4,5]))
