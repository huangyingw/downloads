class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x):
        self.stack.append(x)
        if not self.minstack:
            self.minstack.append(x)
        else:
            y = self.minstack[-1]
            self.minstack.append(min(x, y))

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]

