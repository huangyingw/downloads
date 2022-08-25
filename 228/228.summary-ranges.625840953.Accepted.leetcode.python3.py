class Solution(object):
    def summaryRanges(self, nums):
        start = 0
        result = []
        for idx in range(0, len(nums)):
            if idx + 1 < len(nums) and nums[idx] + 1 == nums[idx + 1]:
                continue
            end = idx
            result.append(str(nums[start]) if start == end else str(nums[start]) + '->' + str(nums[end]))
            start = idx + 1
        return result

