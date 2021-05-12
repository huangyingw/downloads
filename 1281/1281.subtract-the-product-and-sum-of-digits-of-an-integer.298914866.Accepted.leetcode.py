class Solution(object):
    def subtractProductAndSum(self, n):

        from functools import reduce
        from operator import mul
        digits = [int(x) for x in str(n)]
        return reduce(mul, digits) - sum(digits)

