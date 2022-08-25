class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        a, b = 0, 1
        for _ in range(2, N):
            a, b = b, a + b
        return a + b

