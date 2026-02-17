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


clsApp = App([1,2,3,4,5])
print(clsApp._get_add())
print(clsApp._get_event())

