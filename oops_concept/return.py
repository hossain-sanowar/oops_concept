class Return:
    def __init__(self, value):
        self.value = value

    def total(self, a):
        Total=sum(a)
        return Total







clsReturn = Return(5)
print(clsReturn)
print(clsReturn.total([1,2,3]))