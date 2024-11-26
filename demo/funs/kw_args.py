
def fun(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


fun(a = 10, b = 20)
fun(name = 'Abc', age = 20)
