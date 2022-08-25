class Solution(object):
    def combine(self, n, k):
        if k == 0:          # or if k == 1 return [[i] for i in range(1,n+1)]
            return [[]]
        if n < k:           # or if k == n return [[i for i in range(1,n+1)]]
            return []
        without_last = self.combine(n - 1, k)
        with_last = [[n] + combo for combo in self.combine(n - 1, k - 1)]
        return with_last + without_last

