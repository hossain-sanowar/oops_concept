class List:
    def __init__(self, data):
        self.data = data

    def _read_list(self):
        data = []
        for item in self.data:
            data.append(item)
        return data

    def _get_odd(self):
        odd=[]
        for item in self.data:
            if item % 2 != 0:
                odd.append(item)
        return odd


clsList = List([1,2,3,4,5])
print(clsList)
print(clsList._read_list())
print(clsList._get_odd())
