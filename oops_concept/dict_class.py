class DictClass:
    def __init__(self, **kwargs):
        self.data = kwargs

    def __getattr__(self, item):
        return self.data[item]

dictclass=DictClass()
print(dictclass.data)