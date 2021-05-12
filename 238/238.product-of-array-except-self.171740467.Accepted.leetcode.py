class Solution(object):
    def productExceptSelf(self, nums):
        result = [1 for _ in range(len(nums))]

        for idx in range(1, len(nums)):
            result[idx] = result[idx - 1] * nums[idx - 1]

        rightProduct = 1

        for idx in range(len(nums) - 2, -1, -1):
            rightProduct *= nums[idx + 1]
            result[idx] *= rightProduct

        return result

