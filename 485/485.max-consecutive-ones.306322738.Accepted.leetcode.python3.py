class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        ans = 0
        curr = 0
        for n in nums:
            if n == 1:

                curr += 1
                if curr > ans:
                    ans = curr
            else:

                curr = 0
        return ans

