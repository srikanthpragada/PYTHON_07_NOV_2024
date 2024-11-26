#keyword-only args
def wish(*, msg, user):
    print(msg, user.upper())



wish(msg='Hi', user='Steve')
#wish('Mark', 'Hello')
