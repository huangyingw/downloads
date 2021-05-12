class Solution:
    def permute(self, nums):
        res = []
        self.get_permute(res, nums, 0)
        return res

    def get_permute(self, res, nums, index):
        if index == len(nums):
            res.append(list(nums))
            return
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.get_permute(res, nums, index + 1)
            nums[i], nums[index] = nums[index], nums[i]

