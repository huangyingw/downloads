class Solution(object):
    def combine(self, n, k):
        res = []
        self.get_combine(res, [], n, k, 0)
        return res

    def get_combine(self, res, prefix, n, k, start):
        print()
        print("start --> %s" % start)
        print("prefix --> %s" % prefix)
        if k == 0:
            res.append(list(prefix))
            return
        for idx in range(start + 1, n + 1):
            print("idx --> %s" % idx)
            self.get_combine(res, prefix + [idx], n, k - 1, start + 1)

