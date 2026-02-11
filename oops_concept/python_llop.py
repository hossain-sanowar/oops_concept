class Loop:
    def __init__(self,data):
        self.data = data

    def iterate(self):
        for i in self.data:
            yield i
