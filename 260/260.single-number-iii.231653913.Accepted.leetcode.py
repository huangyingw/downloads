class Solution(object):
    def singleNumber(self, nums):
        result = [0 for _ in range(2)]
        result[0] = 0
        result[1] = 0
        n = 0

        for elem in nums:
            n ^= elem

        n = n & (~(n - 1))

        for elem in nums:
            if (elem & n) != 0:
                result[0] ^= elem
            else:
                result[1] ^= elem

        return result

