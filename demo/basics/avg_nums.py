# Take 5 numbers and display avg

total = 0
for i in range(5):
    num = int(input("Enter a number :"))
    total = total + num

print('Average =', total / 5)
