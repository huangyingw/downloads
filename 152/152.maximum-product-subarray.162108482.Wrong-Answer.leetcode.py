class Solution(object):
    def maxProduct(self, nums):
        result = 0
        local = 0

        for num in nums:
            local += num
            result = max(result, local)
            local = max(local, 0)

        return result

