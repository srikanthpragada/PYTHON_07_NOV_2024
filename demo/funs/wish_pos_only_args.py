#Positional-only args
def wish(user, msg, /):
    print(msg, user.upper())



wish('Mark', 'Hello')
#wish('Mark', msg = 'Hi')

