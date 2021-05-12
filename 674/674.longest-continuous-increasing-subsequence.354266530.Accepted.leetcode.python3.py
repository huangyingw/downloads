class Solution(object):
    def findLengthOfLCIS(self, nums):
        longest, current = 0, 0
        for i in range(len(nums)):
            if i == 0 or nums[i] <= nums[i - 1]:
                current = 0
            current += 1
            longest = max(longest, current)
        return longest

