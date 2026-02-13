class Return:
    def __init__(self, value):
        self.value = value

    def total(self, a):
        Total=sum(a)
        return Total

    def even(self, a):
        result=[]
        for i in a:
            if i%2==0:
                result.append(i)
        return result







clsReturn = Return(5)
print(clsReturn)
print(clsReturn.total([1,2,3]))
print(clsReturn.even([1,2,3]))