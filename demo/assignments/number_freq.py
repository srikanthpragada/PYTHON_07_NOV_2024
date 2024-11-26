nums = {}

while True:
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break

    count = nums.get(n, 0)
    nums[n] = count + 1

print(nums)

