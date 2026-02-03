class List:
    def __init__(self,value):
        self.value=value

    def read_list(self):
        self.list=[]
        for item in self.value:
            self.list.append(item)
        return self.list

    def add(self,value):
        self.list.append(value)
        return self.list

    def subtract(self,value):
        self.list.remove(value)
        return self.list

    def read_index(self):
        self.index=[]
        for item in self.list:
            self.index.append(self.list.index(item))
        return self.index


cls=List([1,2,3,4,5])
print(cls.read_list())
print(cls.add(12))
print(cls.subtract(12))
print(cls.read_index())


