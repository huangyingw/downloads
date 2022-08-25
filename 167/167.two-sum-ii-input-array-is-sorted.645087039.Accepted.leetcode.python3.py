class Solution(object):
    def twoSum(self, numbers, target):
        n = {}
        for index, num in enumerate(numbers):
            if target - num in n:
                return [n[target - num] + 1, index + 1]
            n[num] = index

