# print prime numbers between two given numbers

import sys

# Check whether number is given on the command line
if len(sys.argv) < 3:
    print("python primes.py  start  end")
    exit(1)  # Exit with error

start = int(sys.argv[1])
end = int(sys.argv[2])

# start with odd number and ignore all even numbers
if start % 2 == 0:
    start += 1


for num in range(start, end + 1, 2):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            break
    else:
        print(num, end = ' ')

