class Doctor:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def show(self):
        print('Name  : ', self.name)
        print('Dept  : ', self.dept)


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
         pass


r = ResidentDoctor("Dr. James", "Card", 300000)
r.show()
print(r.getsalary())

c = Consultant("Dr. Kim", "Gyn", 10, 1000)



