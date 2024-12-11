try:
    n = int(input("Enter number :"))
    print(100 // n)
except ValueError:
    print('Sorry! Invalid number!')
else:
    print("Else")
finally:
    print('Finally!')

print('The End')
