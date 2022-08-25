class Solution(object):
    def combine(self, n, k):
        res = []
        self.dfs(res, [], n, k, 1)
        return res

    def dfs(self, res, prefix, n, k, start):
        if k == 0:
            res.append(list(prefix))
        for idx in range(start, n + 1):
            self.dfs(res, prefix + [idx], n, k - 1, idx + 1)

