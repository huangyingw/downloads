class Solution(object):
    def permute(self, nums, index=0):
        permutations = []
        if index >= len(nums):
            permutations.append(nums[:])
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            permutations += self.permute_helper(nums, index + 1)
            nums[i], nums[index] = nums[index], nums[i]
        return permutations

