class Solution(object):
    def nthUglyNumber(self, n):

        uglyNumber = [0 for _ in range(n)]
        index = [3]
        factor = [2, 3, 5]
        uglyNumber[0] = 1

        for i in range(1, n):
            minV = min(min(factor[0], factor[1]), factor[2])
            uglyNumber[i] = minV

            if minV == factor[0]:
                factor[0] = 2 * uglyNumber[++index[0]]

            if minV == factor[1]:
                factor[1] = 3 * uglyNumber[++index[1]]

            if minV == factor[2]:
                factor[2] = 5 * uglyNumber[++index[2]]
        return uglyNumber[n - 1]

