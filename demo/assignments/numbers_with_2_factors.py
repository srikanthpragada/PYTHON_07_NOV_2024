def has_more_than_2_factors(num):
    count = 0
    for i in range(2, num//2 + 1):
        if num % i == 0:
            count += 1
            if count == 2:
                return True

    return False

nums = [20, 15, 40, 37, 25]

for n in filter(has_more_than_2_factors, nums):
    print(n)


