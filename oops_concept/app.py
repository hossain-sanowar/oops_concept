class App:
    def __init__(self, data):
        self.data = []

    def _get_add(self):
        data=[]
        for item in self.data:
            data.append(item)

        return data


clsApp = App([1,2,3,4,5])
