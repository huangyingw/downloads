class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        index = cur_sum = 0
        min_length = len(nums) + 1
        for i in range(len(nums)):
            cur_sum += nums[i]
            while cur_sum >= s:
                min_length = min(min_length, i - index + 1)
                cur_sum -= nums[index]
                index += 1
        return min_length if min_length <= len(nums) else 0


class Solution1:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if self.isSumPossible(nums, s, mid):

                high = mid
            else:
                low = mid + 1
        return high + 1 if high < len(nums) else 0

    def isSumPossible(self, nums, s, group_size):
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if i >= group_size:
                if cur_sum >= s:
                    return True
                cur_sum -= nums[i - group_size]
        return False

