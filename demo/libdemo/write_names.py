
names = ['Jack', 'Scott', 'Anders', 'Mike', 'Jackson']

f = open("names.txt", "wt")

for n in names:
    f.write(n + "\n")

f.close()



