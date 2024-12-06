class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def clear(self):
        self.data.clear()

    def length(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0


s = Stack()
print(s.empty())
s.push(10)
s.push(20)
print(s.peek())
print(s.pop())
print(s.length())
