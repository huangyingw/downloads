class Solution:
    def fib(self, N):
        if N == 0:
            return 0
        l = [0, 1]
        for i in range(2, N):
            l.append(l[i - 1] + l[i - 2])
        return l[N - 1] + l[N - 2]

