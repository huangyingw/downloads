class Solution:
    def permute(self, nums, ret=[], permutation=[]):
        if not nums:
            ret.append(permutation)
        for i in range(len(nums)):
            self.permute(nums[:i] + nums[i + 1:], ret, permutation + [nums[i]])
        return ret

