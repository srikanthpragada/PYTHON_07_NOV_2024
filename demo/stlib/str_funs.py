def ismobile(s):
    return len(s) == 10 and s.isdigit()


def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


def count(s, fun):
    count = 0
    for c in s:
        if fun(c):
            count += 1

    return count
