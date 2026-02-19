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

    def _get_even_index(self):
        even=[]
        for item in self.data:
            if item%2==0:
                even.append(item)
        return even

    def _get_odd_index(self):
        odd=[]
        for item in self.data:
            if item%2==1:
                odd.append(item)
        return odd

    def get_div(self):
        div=[]
        for item in self.data:
            if item%2==0:
                div.append(item)
        return div

    def _get_item(self):
        item=[]
        for item in self.data:
            item.append(item)
        return item



clsApp = App([1,2,3,4,5, 6,7,8,9])
print(clsApp._get_add())
print(clsApp._get_event())
print(clsApp._get_odd())
print(clsApp._get_index())
print(clsApp._get_even_index())
print(clsApp._get_odd_index())
print(clsApp.get_div())

