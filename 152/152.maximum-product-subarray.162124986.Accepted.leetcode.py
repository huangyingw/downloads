class Solution(object):
    def maxProduct(self, nums):
        maxPre = nums[0]
        minPre = nums[0]
        maxHere = nums[0]
        minHere = nums[0]
        result = nums[0]

        for idx in range(1, len(nums)):
            maxHere = max(maxPre * nums[idx], minPre * nums[idx], nums[idx])
            minHere = min(maxPre * nums[idx], minPre * nums[idx], nums[idx])
            maxPre = maxHere
            minPre = minHere
            result = max(result, maxHere)

        return result

