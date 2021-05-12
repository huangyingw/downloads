class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = cur_sum = 0
        for number in nums:
            cur_sum += number
            if cur_sum < min_sum:
                min_sum = cur_sum
        return abs(min_sum) + 1

