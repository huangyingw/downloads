class MyQueue(object):
    def __init__(self):
        self.stack = []
        self.reversedStack = []
        self.top = None

    def push(self, x):
        if not self.stack:
            self.top = x
        self.stack.append(x)

    def pop(self):
        if not self.reversedStack:
            while self.stack:
                self.reversedStack.append(self.stack.pop())
        return self.reversedStack.pop()

    def peek(self):
        if self.reversedStack:
            return self.reversedStack[-1]
        return self.top

    def empty(self):
        return not self.stack and not self.reversedStack

