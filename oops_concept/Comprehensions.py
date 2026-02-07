'''squares=[x*x for x in range(10)]
print(squares)

squares_dict={x*x for x in range(10)}
print(squares_dict)'''

'''uniques_value={f(x) for x in data}
print(uniques_value)'''

'''lst =[x*x for x in range(10**6)]
print(lst)
gen =(x*x for x in range(10**6))
print(gen)'''

'''results=[]
for x in range(1_000_000):
    results.append(x*x )
print(results)'''


import math
points=[(1,2),(3,4),(5,6),(7,8),(9,10)]
distances=[]
for x,y in points:
    d=math.sqrt(x**2+y**2)
    distances.append(d)
print(distances)

'''import numpy as np
arr =np.arange(1_000_000)
results=arr*arr
print(results)'''

class List:
    def __init__(self,lst):
        self.lst=lst

    def read_list(self):
        for item in self.lst:
            print(item)
clsList=List([1,2,3,4,5])
clsList.read_list()


class List2:
    def __init__(self,lst):
        self.lst=lst

    def read_list(self):
        for item in self.lst:
            print(item)

    def add_index(self):
        index=[]
        for item in self.lst:
            index.append(item)
        return index

    def indexing(self):
        index=self.add_index()
        print(index)


clsList2=List2([1,2,3,4,5])
clsList2.read_list()
clsList2.add_index()


class List3:
    def __init__(self,lst):
        self.lst=lst

    def get_index_5(self):
        for item in self.lst:
            if item==5:
                return item

    def add_index(self):
        add=[]
        for item in self.lst:
            print(item)
            if item==1 or item==2:
                add.append(item)
        return add



clsList3=List3([1,2,3,4,5])
print(clsList3.get_index_5())
print(clsList3.add_index())


