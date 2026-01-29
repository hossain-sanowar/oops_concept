class lsitItem:
    def __init__(self, data):
        self.data = data

    def read(self):
        return self.data


clslist = lsitItem([1,2,3,4,5])
print(clslist.read())