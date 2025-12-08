from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name):
        self.id=id
        self.name = name

    @abstractmethod
    def get_salary(self):
        raise NotImplementedError()


class FullTimeEmployee(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.salary=salary


    def get_salary(self):
        return self.salary


class PartTimeEmployee(Employee):
    def __init__(self, id, name, hourly_rate, total_hour):
        super().__init__(id, name)
        self.hourly_rate=hourly_rate
        self.total_hour=total_hour


    def get_salary(self):
        return self.hourly_rate*self.total_hour


class HR:
    def __init__(self, employees:list[Employee]):
        self.employees=employees

    def get_total_salary(self):
        salary=0
        for employee in self.employees:
            salary += employee.get_salary()

        return salary

e1=FullTimeEmployee(id="e1", name="E1", salary=1200)
e2=PartTimeEmployee(id="e2", name="E2", hourly_rate=100, total_hour=10)
print(e1.get_salary())
print(e2.get_salary())

print("-----------")
employee_list=[e1, e2]
hrl=HR(employee_list)
print(hrl.get_total_salary())
print("end of the program")