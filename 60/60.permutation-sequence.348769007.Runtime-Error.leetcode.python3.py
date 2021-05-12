class Solution(object):
    def getPermutation(self, n, k):
        remain = range(1, n + 1)
        if k <= 1:
            return ''.join(str(t) for t in remain)
        total = 1
        for num in remain:
            total *= num
        res = self.do_getPermutation(remain, total, n - 1, k - 1)
        return ''.join(str(t) for t in res)

    def do_getPermutation(self, remain, curr, n, k):
        if n == 0 or k <= 0 or curr == 0:
            return remain
        step = k // curr
        k %= curr
        curr //= n
        res = [remain[step]] + self.do_getPermutation(remain[:step] + remain[step + 1:], curr, n - 1, k)
        return res

