
total = count = 0

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break
    # Negative number, ignore it
    if num < 0:
        continue

    # positive number, so process it
    total = total + num
    count = count + 1

print('Average = ', total // count)
