class List:
    def __init__(self,value):
        self.value=value

    def read_list(self):
        self.list=[]
        for item in self.value:
            self.list.append(item)
        return self.list
