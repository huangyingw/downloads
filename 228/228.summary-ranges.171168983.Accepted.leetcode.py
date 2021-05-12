class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []

        end = nums[0]
        start = end
        result = []

        for idx in range(len(nums)):
            if idx + 1 < len(nums) and nums[idx] + 1 == nums[idx + 1]:
                continue

            end = nums[idx]
            result.append(str(start) if start == end else str(start) + '->' + str(end))

            if idx + 1 < len(nums):
                start = nums[idx + 1]

        return result

