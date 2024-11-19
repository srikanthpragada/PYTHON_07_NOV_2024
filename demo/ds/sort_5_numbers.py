nums = []  # empty list

for i in range(5):
    n = int(input("Enter number :"))
    nums.append(n)

nums.sort()

for n in nums:
    print(n, end=' ')
