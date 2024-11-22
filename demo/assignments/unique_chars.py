
names = ['andy','mark', 'jack','jason', 'marin']

chars = set()   # Empty set 
for name in names:
    chars = chars | set(name)

print(chars)
