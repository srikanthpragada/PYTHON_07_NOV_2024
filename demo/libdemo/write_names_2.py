names = ['Jack', 'Scott', 'Anders', 'Mike', 'Jackson']

with open("names.txt", "wt") as f:
    for n in names:
        f.write(n + "\n")
