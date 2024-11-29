def isvalidname(name):
    for c in name:
        if not (c.isalpha() or c == ' '):
            return False

    return True

names = []

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    names.append(name)

for n in sorted(filter(isvalidname, names)):
    print(n)
