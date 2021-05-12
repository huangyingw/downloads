class Solution(object):
    memo = [0, 1]

    def numSquares(self, n):
        while len(self.memo) <= n:
            self.memo += [1 + min(self.memo[-i * i] for i in range(1, int(len(self.memo)**0.5) + 1))]
        return self.memo[n]

