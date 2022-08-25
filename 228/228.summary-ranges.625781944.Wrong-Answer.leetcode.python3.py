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
                print("end --> %s" % end)
                continue
            result.append(str(start) if start == end else str(start) + '->' + str(end))
            start = nums[idx]
            print("start --> %s" % start)
            end = nums[idx]
            print("end --> %s" % end)
        if start == end:
            result.append(str(start))
        return result

