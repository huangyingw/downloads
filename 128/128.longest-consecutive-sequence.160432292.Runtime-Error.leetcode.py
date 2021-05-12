class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        result = 0

        for num in nums:
            count = 1

            if num in numSet:
                right = num + 1

                while right in numSet:
                    count += 1
                    right += 1
                    numSet.remove(right)
                left = num - 1

                while left in numSet:
                    count += 1
                    left -= 1
                    numSet.remove(left)
                numSet.remove(num)
            result = max(result, count)
        return result

