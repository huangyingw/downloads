class Solution(object):
    def combine(self, n, k):
        res = []
        self.get_combine(res, [], n, k, 1)
        return res

    def get_combine(self, res, prefix, n, k, start):
        if k == 0:
            res.append(list(prefix))
        elif start <= n:
            prefix.append(start)
            self.get_combine(res, prefix, n, k - 1, start + 1)
            prefix.pop()
            self.get_combine(res, prefix, n, k, start + 1)

