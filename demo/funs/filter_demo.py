def iseven(n):
    return n % 2 == 0

nums = [1, 3, 4, 5, 2, 10]

for n in filter(iseven, nums):
    print(n)



