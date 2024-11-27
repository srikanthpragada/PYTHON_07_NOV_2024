def reverse(st):
    return st[::-1]


for n in map(reverse, ['Ben', 'Joe', 'Kevin']):
    print(n)

for n in map(len, ['Ben', 'Joe', 'Kevin']):
    print(n)
