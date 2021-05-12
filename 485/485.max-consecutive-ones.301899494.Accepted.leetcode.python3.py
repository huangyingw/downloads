class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        count = 0
        for n in nums:
            if n:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
        return max_count

