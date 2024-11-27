# Function is treated as an object
def hello():
    print('Hello')


st = "abc"
print(type(st))
print(type(hello))

st2 = st
hello2 = hello

print(st2)
hello2()
