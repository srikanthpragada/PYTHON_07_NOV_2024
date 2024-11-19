
s = "Abc123Xyz45Pqr"

for c in s:
    if c.isdigit():
        print('.', end='')
    else:
        print(c, end = '')

