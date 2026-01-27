class DictClass:
    def __init__(self, **kwargs):
        self.data = kwargs

    def __getattr__(self, item):
        return self.data[item]

data={"key":'value'}
dictclass=DictClass(data=data)
print(dictclass.data.values())


class listRead:
    def __init__(self, data):
        self.data = data

    def read_list(self):
        data_store=[]
        for item in self.data:
            data_store.append(item)

listClass=listRead([1,3,4,5,6,8])
print(listClass.read_list())