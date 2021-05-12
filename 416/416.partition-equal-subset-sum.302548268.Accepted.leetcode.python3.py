from collections import Counter


class Solution(object):
    def canPartition(self, nums):
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        freq = Counter(nums)
        return self.partition(freq, nums_sum // 2)

    def partition(self, freq, target):
        if target == 0:
            return True
        if target < 0:
            return False
        for num in freq:
            if freq[num] == 0:
                continue
            freq[num] -= 1
            if self.partition(freq, target - num):
                return True
            freq[num] += 1
        return False

