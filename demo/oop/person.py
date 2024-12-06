class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __repr__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        print('__gt__')
        return self.age > other.age

    def __int__(self):
        return self.age


p1 = Person("Bill", 40)
p2 = Person("Scott", 30)
p3 = Person("Bill", 40)
p4 = Person("Peter", 20)

people = [p1, p2, p3, p4]
print(sorted(people))

print(p1)
print(str(p1))
print(p1.__str__())
print(p1 == p3)  # p1.__eq__(p3)
print(p1 > p2)  # p1.__gt__(p2)
print(p1 == p2)
