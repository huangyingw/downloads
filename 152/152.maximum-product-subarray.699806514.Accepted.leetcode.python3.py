class Solution(object):
    def maxProduct(self, nums):
        max_so_far, min_so_far, result = nums[0], nums[0], nums[0]
        for index in range(1, len(nums)):
            if nums[index] > 0:
                max_so_far = max(max_so_far * nums[index], nums[index])
                min_so_far = min(min_so_far * nums[index], nums[index])
            else:
                temp = max_so_far
                max_so_far = max(min_so_far * nums[index], nums[index])
                min_so_far = min(temp * nums[index], nums[index])
            result = max(result, max_so_far)
        return result

