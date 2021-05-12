class Solution:
    def fib(self, N):
        i, j = 0, 1
        for _ in range(N):
            i, j = j, i + j
        return i

