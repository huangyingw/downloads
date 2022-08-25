class Solution(object):
    def combine(self, n, k):
        def helper(left, right, k):
            if k == 0:
                result.append(list(current))
            for index in range(left, right + 1):
                current.append(index)
                helper(index + 1, right, k - 1)
                current.pop()
        current = []
        result = []
        helper(1, n, k)
        return result

