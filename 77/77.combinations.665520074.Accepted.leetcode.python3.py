class Solution(object):
    def combine(self, n, k):
        if k == 0:
            return [[]]
        if n < k:
            return []
        without_last = self.combine(n - 1, k)
        with_last = [[n] + combo for combo in self.combine(n - 1, k - 1)]
        return with_last + without_last

