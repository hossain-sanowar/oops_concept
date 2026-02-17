class App:
    def __init__(self, data):
        self.data = data

    def _get_add(self):
        add=[]
        for item in self.data:
            add.append(item)
        return add

    def _get_event(self):
        event=[]
        for item in self.data:
            if item%2==0:
                event.append(item)
        return event

    def _get_odd(self):
        odd=[]
        for item in self.data:
            if item%2==1:
                odd.append(item)
        return odd

    def _get_index(self):
        index=[]
        for item in self.data:
            index.append(item)
        return index


clsApp = App([1,2,3,4,5])
print(clsApp._get_add())
print(clsApp._get_event())
print(clsApp._get_odd())

