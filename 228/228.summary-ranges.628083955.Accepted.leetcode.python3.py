class Solution(object):
    def summaryRanges(self, nums):
        start = 0
        result = []
        for idx in range(len(nums)):
            if idx + 1 < len(nums) and nums[idx] + 1 == nums[idx + 1]:
                continue
            result.append(str(nums[start]) if start == idx else str(nums[start]) + '->' + str(nums[idx]))
            start = idx + 1
        return result

