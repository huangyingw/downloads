class Solution:
    def wiggleSort(self, nums):
        for i in range(len(nums) - 1):
            if i % 2 == 0 and nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

