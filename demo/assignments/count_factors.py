# Take a number and display factors count

num = int(input("Enter a number :"))

count = 0
for i in range(2, num // 2 + 1):
    if num % i == 0:
         count += 1   # count = count + 1

print(f"Count = {count}")

