class Employee:
    def __init__(self, name, salary):
        self.name = name
        # private attribute
        self.__salary = salary

    def getsalary(self):
        return self.__salary


e = Employee("Jack", 100000)
print(e.name)
print(e.getsalary())
print(e.__dict__)
print(e._Employee__salary)
