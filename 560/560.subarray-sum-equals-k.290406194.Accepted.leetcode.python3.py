class Solution(object):
    def subarraySum(self, nums, k):
        sum_map = {}
        sum_map[0] = 1
        count = curr_sum = 0
        for num in nums:
            curr_sum += num
            count += sum_map.get(curr_sum - k, 0)
            sum_map[curr_sum] = sum_map.get(curr_sum, 0) + 1
        return count

