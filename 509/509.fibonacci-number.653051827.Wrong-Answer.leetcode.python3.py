class Solution:
    def fib(self, N):
        m = 0
        n = 1
        for i in range(N - 1):
            temp = m + n
            m = n
            n = temp
        return n

