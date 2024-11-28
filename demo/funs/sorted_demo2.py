def extract_number(s):
    return int(s[1:])


codes = ['E123', 'X83', 'A233', 'D111', 'X9']

for c in sorted(codes, key = extract_number):
    print(c)



