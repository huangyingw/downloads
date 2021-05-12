class Solution(object):
    def combinationSum3(self, k, n):
        current = []
        result = []

        def dfs(start, k, n):
            if k < 0 or n < 0:
                return

            if k == 0 and n == 0:
                result.append(list(current))

            for idx in range(start, 10):
                current.append(idx)
                dfs(idx + 1, k - 1, n - idx)
                current.pop()

        dfs(1, k, n)
        return result

