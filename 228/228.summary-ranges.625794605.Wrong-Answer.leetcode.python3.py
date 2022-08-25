class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        start = nums[0]
        result = []
        for idx in range(1, len(nums)):
            if nums[idx - 1] + 1 == nums[idx]:
                continue
            end = nums[idx - 1]
            print("end --> %s" % end)
            result.append(str(start) if start == end else str(start) + '->' + str(end))
            start = nums[idx]
            print("start --> %s" % start)
        result.append(str(start) if start == end else str(start) + '->' + str(end))
        return result

