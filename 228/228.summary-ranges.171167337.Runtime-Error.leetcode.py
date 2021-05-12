class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []

        end = nums[0]
        start = end
        print('start --> %s' % start)
        result = []

        for idx in range(len(nums)):
            print('nums[idx] --> %s' % nums[idx])
            if nums[idx] == nums[idx + 1]:
                continue

            else:
                start = end
                print('start --> %s' % start)
                end = nums[idx]
                print('end --> %s' % end)
                result.append(str(start) if start == end else str(start) + '->' + str(end))

        return result

