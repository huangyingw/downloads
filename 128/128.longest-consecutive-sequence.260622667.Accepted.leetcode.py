class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        result = 0
        for num in nums:
            count = 1
            if num in numSet:
                right = num + 1
                while right in numSet:
                    numSet.remove(right)
                    count += 1
                    right += 1
                left = num - 1
                while left in numSet:
                    numSet.remove(left)
                    count += 1
                    left -= 1
                numSet.remove(num)
            result = max(result, count)
        return result

