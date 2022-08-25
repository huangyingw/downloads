class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        start = end = 0
        result = []
        for idx in range(len(nums)):
            if idx + 1 < len(nums) and nums[idx] + 1 == nums[idx + 1]:
                continue
            end = idx
            print("end --> %s" % nums[end])
            result.append(str(nums[start]) if start == end else str(nums[start]) + '->' + str(nums[end]))
            if end + 1 < len(nums):
                start = end + 1
                print("start --> %s" % nums[start])
        return result

