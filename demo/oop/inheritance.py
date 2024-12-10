from abc import ABC, abstractmethod


# Abstract class
class Doctor(ABC):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def show(self):
        print('Name  : ', self.name)
        print('Dept  : ', self.dept)

    # Abstract method
    @abstractmethod
    def getsalary(self):
        pass


class ResidentDoctor(Doctor):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    def show(self):
        super().show()
        print('Salary : ', self.salary)

    def getsalary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, dept, visits, charge):
        super().__init__(name, dept)
        self.visits = visits
        self.charge = charge

    def show(self):
        super().show()
        print('Visits : ', self.visits)
        print('Charge : ', self.charge)

    def getsalary(self):
        return self.visits * self.charge


#d  = Doctor("a", "b")

r = ResidentDoctor("Dr. James", "Card", 300000)
r.show()
print(r.getsalary())

c = Consultant("Dr. Kim", "Gyn", 10, 1000)
c.show()
print(c.getsalary())
