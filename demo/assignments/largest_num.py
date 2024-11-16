# Take numbers until 0 is given and display the largest

largest = 0
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break   # terminate the loop

    if num > largest:
        largest = num



print('Largest =', largest)
