class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.input.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.output.pop(-1)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.output:
            while self.input:
                self.output.append(self.input[-1])
        return self.output[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.input and not self.output

