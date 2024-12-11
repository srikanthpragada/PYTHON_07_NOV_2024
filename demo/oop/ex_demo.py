try:
    n = int(input("Enter number :"))
    print(100 // n)
except ValueError:
    print('Sorry! Invalid number!')
except ZeroDivisionError:
    print('Sorry! Number cannot be zero!')

print('The End')
