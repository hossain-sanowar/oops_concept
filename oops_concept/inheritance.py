class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

class HR(Student):
    def __init__(self, name, age, total_hour):
        super().__init__(name, age)
        self.name=name
        self.total_hour=total_hour
        self.total_salary=10

    def get_total_salary(self):
        return self.total_salary*self.total_hour



stu=Student("John", 25)
print(stu.get_age())
print(stu.get_name())

hr=HR("John", 25)
print(hr.get_total_salary())