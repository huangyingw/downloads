class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        n = self.stack.pop()
        if self.min_stack[-1] == n:
            self.min_stack.pop()
        return n

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

