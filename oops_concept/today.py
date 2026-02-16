class List:
    def __init__(self, data):
        self.data = data

    def _read_list(self):
        data = []
        for item in self.data:
            data.append(item)
        return data


clsList = List([1,2,3,4,5])
print(clsList)
print(clsList._read_list())
