try:
    n = int(input("Enter number :"))
    print(100 // n)
except ValueError:
    print('Sorry! Invalid number!')
except Exception as ex:
    print('Error -> ' + str(ex))

print('The End')
