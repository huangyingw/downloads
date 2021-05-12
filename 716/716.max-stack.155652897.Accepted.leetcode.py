class MaxStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.max = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        if not self.max or self.max[-1] <= x:
            self.max.append(x)

    def pop(self):
        """
        :rtype: int
        """
        temp = self.data.pop()
        if temp == self.max[-1]:
            self.max.pop(-1)
        return temp

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max[-1]

    def popMax(self):
        """
        :rtype: int
        """
        max = self.peekMax()
        buffer = []
        while self.top() != max:
            buffer.append(self.pop())
        self.pop()
        while buffer:
            self.push(buffer.pop())
        return max

