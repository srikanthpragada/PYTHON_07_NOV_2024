# Global variable
g = 10

def f1():
    global  g
    a = 100  # Enclosing variable
    g = 1000

    # local function or nested function
    def f2():
        nonlocal a
        b = 200  # Local variable
        a = 1
        print(g, a, b)

    f2()
    print(a)

f1()