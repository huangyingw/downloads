from operator import add


class Solution:
    def generate(self, numRows):
        result = [[1]]
        for i in range(1, numRows):
            ll = map(add, result[-1] + [0], [0] + result[-1])
            result += [list(ll)]
        return result if numRows else []

