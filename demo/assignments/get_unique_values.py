def get_unique_values(lst):
    ulist = []
    for v in lst:
        if v not in ulist:
            ulist.append(v)

    return ulist


print(get_unique_values([10, 20, 10, 5, 30]))
print(get_unique_values(['Ben','Joe',"Jack", 'Ben', 'Bill', 'Kevin']))
