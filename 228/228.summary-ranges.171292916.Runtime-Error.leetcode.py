class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []

        start = nums[0]
        result = []

        for idx in range(1, len(nums) + 1):
            if idx < len(nums) and nums[idx - 1] + 1 == nums[idx]:
                continue

            end = idx - 1
            result.append(str(nums[start]) if start == end else str(nums[start]) + '->' + str(nums[end]))

            if idx < len(nums):
                start = idx

        return result

