# type hints
def add(v1 : int, v2 : int) -> int:
    return v1 + v2


print(add(10, 20))
print(add('Abc', 'Xyz'))

print(add.__annotations__)


