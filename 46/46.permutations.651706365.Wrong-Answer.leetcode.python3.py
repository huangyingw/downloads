class Solution:
    def permute(self, nums, ret=[], permutation=[]):
        if not nums:
            print("permutation --> %s" % permutation)
            ret.append(permutation)
        for i in range(len(nums)):
            self.permute(nums[:i] + nums[i + 1:], ret, permutation + [nums[i]])
        print("ret --> %s" % ret)
        return ret

