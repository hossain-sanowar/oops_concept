class DictClass:
    def __init__(self, **kwargs):
        self.data = kwargs

    def __getattr__(self, item):
        return self.data[item]

data={"key":'value'}
dictclass=DictClass(data=data)
print(dictclass.data.values())


class listRead:
    def __init__(self):
        self.data = []

