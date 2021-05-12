class MyStack:
    def __init__(self):
        self.stack1 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        return self.stack1.pop()

    def top(self):
        return self.stack1[-1]

    def empty(self):
        return not len(self.stack1)

