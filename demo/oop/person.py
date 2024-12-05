class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Bill", 40)
p2 = Person("Scott", 30)
p3 = Person("Bill", 40)

print(p1)
print(p1 == p3)
#print(p1 > p2)
