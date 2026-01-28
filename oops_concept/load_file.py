#from dict_class import listRead
#from oops_concept.dict_class import listRead

#listclass=listRead([3,4,5,6,8])
#print(listclass.read_list2())

class listWrite:
    def __init__(self, data):
        self.data = data

    def write(self):
        get_data = []
        for item in self.data:
            get_data.append(item)
        return get_data

    def read(self):
        get_data_write=self.write()
        if len(get_data_write)>0:
            return get_data_write


cls_write = listWrite([3,4,5,6,8])
print(cls_write.write())