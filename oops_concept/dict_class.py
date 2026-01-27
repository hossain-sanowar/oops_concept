class DictClass:
    def __init__(self, **kwargs):
        self.data = kwargs

dictclass=DictClass()
print(dictclass.data)