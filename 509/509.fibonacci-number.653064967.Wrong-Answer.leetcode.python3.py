class Solution:
    def fib(self, N):
        l = [0, 1]
        for i in range(2, N):
            l.append(l[i - 1] + l[i - 2])
            print("l --> %s" % l)
        return l[N - 1] + l[N - 2]

