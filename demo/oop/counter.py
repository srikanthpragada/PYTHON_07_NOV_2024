class Counter:
    def __init__(self, start=0):
        # Object attributes
        self.start = start
        self.value = start

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

    def getValue(self):
        return self.value

    def reset(self):
        self.value = self.start


c = Counter()
c.inc()
c.inc()
print(c.getValue())
c.reset()
print(c.getValue())

c2 = Counter(100)
c2.dec()
print(c2.getValue())
