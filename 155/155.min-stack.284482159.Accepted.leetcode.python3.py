class MinStack(object):
    def __init__(self):
        self.data = []
        self.mins = []

    def push(self, x):
        self.data.append(x)
        if not self.mins or self.mins[-1] >= x:
            self.mins.append(x)

    def pop(self):
        if self.data.pop() == self.mins[-1]:
            self.mins.pop()

    def top(self):
        return self.data[-1]

    def getMin(self):
        return self.mins[-1]

