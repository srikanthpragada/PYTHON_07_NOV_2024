import threading

class PrintThread(threading.Thread):
    def run(self):
        for n in range(10):
            print(f'Print {n}')


pt = PrintThread()
pt.start()

for n in range(10):
    print(f'Main {n}')