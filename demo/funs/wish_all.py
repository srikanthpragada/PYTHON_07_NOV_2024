
def wish(*users, msg = 'Hi'):
    for name in users:
        print(msg, name)



wish('Scott', 'Jack', 'Tom', msg = 'Hello')
wish('Steve','Mark')

