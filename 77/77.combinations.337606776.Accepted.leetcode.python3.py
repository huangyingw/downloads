class Solution(object):
    def combine(self, n, k):
        res = []
        self.get_combine(res, [], n, k, 1)
        return res

    def get_combine(self, res, prefix, n, k, start):
        if k == 0:
            res.append(list(prefix))
        for idx in range(start, n + 1):
            prefix.append(idx)
            self.get_combine(res, prefix, n, k - 1, idx + 1)
            prefix.pop()

