
def numbers():
    for n in range(1, 11):
        yield  n


num = numbers()
print(type(num))

print(next(num))
print(next(num))
