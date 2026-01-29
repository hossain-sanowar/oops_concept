class lsitItem:
    def __init__(self, data):
        self.data = data

    def read(self):
        return self.data

    def get_even(self):
        even = []
        for item in self.data:
            if item % 2 == 0:
                even.append(item)
        return even

    def get_odd(self):
        odd = []
        for item in self.data:
            if item % 2 != 0:
                odd.append(item)
        return odd


clslist = lsitItem([1,2,3,4,5])
print(clslist.read())
print(clslist.get_even())
print(clslist.get_odd())