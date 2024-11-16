# Take a number and smallest factor other than 1

num = int(input("Enter a number :"))

for i in range(num // 2, 0, -1):
    if num % i == 0:
        print(i)
        break
