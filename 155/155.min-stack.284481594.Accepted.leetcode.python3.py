class MinStack:
    def __init__(self):
        self.stack = []
        self.minV = float('inf')

    def push(self, x):
        self.minV = min(x, self.minV)
        self.stack.append((x, self.minV))

    def pop(self):
        if self.stack:
            self.stack.pop()
        self.minV = self.stack[-1][1] if self.stack else float('inf')
        return

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.minV

