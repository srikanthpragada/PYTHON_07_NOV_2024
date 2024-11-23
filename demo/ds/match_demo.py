
d = { 'p1' : 10, 'p2' : 20}

match d:
    case {'x' : v}:
        print(v)
    case {'p1' : v}:
        print(v)
    case _:
        print('Not found')



