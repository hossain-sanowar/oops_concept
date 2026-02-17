class App:
    def __init__(self, data):
        self.data = data

    def _get_add(self):
        add=[]
        for item in self.data:
            add.append(item)

        return add


clsApp = App([1,2,3,4,5])
print(clsApp._get_add())

