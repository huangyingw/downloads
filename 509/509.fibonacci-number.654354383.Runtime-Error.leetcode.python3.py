class Solution:
    def fib(self, N):
        if N < 2:
            return N
        l = [0, 1]
        for i in range(2, N):
            l.append(l[i - 1] + l[i - 2])
        return l[N]

