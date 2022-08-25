class Solution(object):
    def longestConsecutive(self, nums):
        numset = set(nums)
        longest = 0
        for num in numset:
            if num - 1 in numset:
                continue
            seq = 0
            while num in numset:
                seq += 1
                num += 1
            longest = max(longest, seq)
        return longest

