class list_data:
    def __init__(self,data):
        self.data = data

    def get_even(self):
        even = []
        for item in self.data:
            even.append(item)
        return even

clslist=list_data([1,2,3,4,5,6])
print(clslist.get_even())