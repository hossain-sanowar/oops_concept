class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

stu=Student("John", 25)
print(stu.get_age())
print(stu.get_name())