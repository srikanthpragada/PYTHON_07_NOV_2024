
names = ['andy','mark', 'jack','jason', 'marin']

chars = set(names[0])   # Set for first name

for name in names[1:]:
    chars = chars & set(name)

print(chars)
