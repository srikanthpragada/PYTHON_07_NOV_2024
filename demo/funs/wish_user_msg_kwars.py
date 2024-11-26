# function with parameter
def wish(user, msg):
    print(msg, user.upper())


# positional args
wish('Scott', 'Good Morning')

# keyword args
wish(msg='Hi', user='Steve')

# wish(msg = 'Hello')
