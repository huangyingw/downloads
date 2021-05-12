class Solution(object):
    def summaryRanges(self, nums):
        end = nums[0]
        start = end
        result = []
        for idx in range(1, len(nums)):
            if nums[idx] == end + 1:
                end += 1
                continue
            result.append(start if start == end else start + '->' + end)
        return result

