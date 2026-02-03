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
        self.list.append(value)
        return self.list


cls=List([1,2,3,4,5])
print(cls.read_list())
print(cls.add(12))
