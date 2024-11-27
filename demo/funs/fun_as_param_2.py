def show(msg):
    print(msg)

def task(fun, msg):
    fun(msg)


task(show, 'Hello')
task(show, 'Hi')
