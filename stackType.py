class Stack(object):
    def __init__(self):
        self.stack = []
        self.size = 0

    def queue(self, x):
        self.stack.append(x)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.stack.pop(-1)

    def last_item(self):
        return self.stack[-1]
