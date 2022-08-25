class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        end = nums[0]
        start = end
        result = []
        for idx in range(1, len(nums)):
            if nums[idx] == end + 1:
                end += 1
                continue
            result.append(start if start == end else start + '->' + end)
            start = nums[idx]
            end = nums[idx]
        result.append(start if start == end else start + '->' + end)
        return result

