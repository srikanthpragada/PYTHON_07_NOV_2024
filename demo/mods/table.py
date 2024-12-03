# print table by taking  a number and optional length on command-line

import sys

# Check whether number is given on the command line
if len(sys.argv) < 2:
    print("Sorry! Number is missing!")
    exit(1)  # Exit with error

size = 10
if len(sys.argv) == 3:
    size = int(sys.argv[2])

num = int(sys.argv[1])  # Take command-line argument

for n in range(1, size + 1):
    print(f"{num:3} * {n:2} = {n * num:5}")
