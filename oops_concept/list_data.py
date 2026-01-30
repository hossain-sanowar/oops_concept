class list_data:
    def __init__(self,data):
        self.data = data

    def get_even(self):
        even = []
        for item in self.data:
            even.append(item)
        return even

    def get_odd(self):
        odd = []
        for item in self.data:
            if item % 2 != 0:
                odd.append(item)
        return odd

    def index(self):
        data = self.data[1]+self.data[2]
        return data

    def add_even(self):
        add_even = []
        sum=0
        for item in self.data:
            if item % 2 == 0:
                sum=sum+item
                add_even.append(item)
        return sum

    def add_odd(self):
        odd_sum=0
        for item in self.data:
            if item % 2 ==1:
                odd_sum=odd_sum+item
        return odd_sum




clslist=list_data([1,2,3,4,5,6])
print(clslist.get_even())
print(clslist.get_odd())
print(clslist.index())
print(clslist.add_even())
print(clslist.add_odd())