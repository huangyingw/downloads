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
            result.append(str(start) if start == end else str(start) + '->' + str(end))
        return result

