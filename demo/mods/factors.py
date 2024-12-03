# print factors by taking  a number on command-line

import sys

# Check whether number is given on the command line
if len(sys.argv) < 2:
    print("Sorry! Number is missing!")
    exit(1)  # Exit with error

num = int(sys.argv[1])  # Take command-line argument

for n in range(2, num // 2 + 1):
    if num % n == 0:
        print(n, end=' ')
