
names = ['Jack','Mark','Scott','Jack', "Scott", 'Andy', 'Bill', 'Andy']

freq_dict = {}

for name in sorted(set(names)):
    freq_dict[name] = names.count(name)

print(freq_dict)