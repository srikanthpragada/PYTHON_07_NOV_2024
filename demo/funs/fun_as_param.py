def hello():
    print('Hello')

def goodbye():
    print('Good Bye!')

def task(fun):
    fun()


task(hello)
task(goodbye)