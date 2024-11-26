
def table(num, size = 10):
    for n in range(1, size + 1):
        print(f"{num:3} * {n:2} = {num * n:5}")

table(15, 5)
table(23)
