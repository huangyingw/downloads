class Solution(object):
    def nextPermutation(self, nums):
        print('def nextPermutation --> ')
        index_i = len(nums) - 2
        while index_i >= 0 and nums[index_i] >= nums[index_i + 1]:
            index_i -= 1
        if index_i >= 0:
            index_j = len(nums) - 1
            while index_j >= index_i and nums[index_j] <= nums[index_i]:
                index_j -= 1
            nums[index_i], nums[index_j] = nums[index_j], nums[index_i]
        start = index_i + 1
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

