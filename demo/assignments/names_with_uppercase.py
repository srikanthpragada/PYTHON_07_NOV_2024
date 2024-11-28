def has_upper(st):
    for ch in st:
        if ch.isupper():
            return True

    return False


names = ['scott', 'Jack', 'mark', 'Tom']

for n in filter(has_upper, names):
    print(n)
