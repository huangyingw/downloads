class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        buf = []

        while self.stack:
            buf.append(self.stack.pop(-1))

        self.stack.append(x)

        while buf:
            self.stack.append(buf.pop(-1))

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return not self.stack

