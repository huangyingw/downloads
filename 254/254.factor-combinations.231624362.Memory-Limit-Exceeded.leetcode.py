class Solution(object):
    def getFactors(self, n):
        ret = []
        self.dfs(ret, [], n, 2)
        return ret

    def dfs(self, ret, item, n, start):
        if n == 1:
            if len(item) > 1:
                ret.append(list(item))

        for i in range(start, n + 1):
            if n % i == 0:
                item.append(i)
                self.dfs(ret, item, n / i, i)
                item.pop()

