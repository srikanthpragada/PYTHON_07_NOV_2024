# function with parameter
def wish(user = 'Guest', msg = 'Hello'):
    print(msg, user.upper())

# positional args
wish('Scott', 'Good Morning')

# keyword args
wish(msg = 'Hi', user = 'Steve')

wish('Tom')
wish(user = 'Jack')
wish(msg = 'Hi')





