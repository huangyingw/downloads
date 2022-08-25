class Solution(object):
    def combine(self, n, k):
        res = []
        self.get_combine(res, [], n, k, 1)
        return res

    def get_combine(self, res, prefix, n, k, start):
        print("prefix --> %s" % prefix)
        if k == 0:
            res.append(list(prefix))
            return
        for idx in range(start, n + 1):
            self.get_combine(res, prefix + [idx], n, k - 1, start + 1)

