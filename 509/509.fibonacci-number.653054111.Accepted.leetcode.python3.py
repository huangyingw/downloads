class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        cache = {0: 0, 1: 1}
        for i in range(2, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[N]

