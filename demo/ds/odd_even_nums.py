odds = []
evens = []
while True:
    num = int(input("Enter num [stop if 0 ]:"))
    if num == 0:
        break
    if num % 2 != 0:
        odds.append(num)
    else:
        evens.append(num)

for n in odds + evens:
    print(n, end=' ')
