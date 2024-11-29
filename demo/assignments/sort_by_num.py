def extract_number(s):
    n = ""
    for c in s:
        if c.isdigit():
            n += c

    return int(n)


data = ['A123', 'X20', 'B12C5', 'P9Q2']

for v in sorted(data, key=extract_number):
    print(v)
