class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        start = nums[0]
        end = nums[0]
        result = []
        for idx in range(1, len(nums)):
            if nums[idx - 1] + 1 == nums[idx]:
                end = nums[idx]
                print("end --> %s" % end)
                continue
            result.append(str(start) if start == end else str(start) + '->' + str(end))
            start = nums[idx]
            end = nums[idx]
            print("start --> %s" % start)
        result.append(str(start) if start == end else str(start) + '->' + str(end))
        return result

