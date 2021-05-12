class Solution:
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

    def repeatedStringMatch(self, A, B):
        if set(A) != set(B):
            if len(A) < len(B):
                return -1

        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q + i):
                return q + i
        return -1

