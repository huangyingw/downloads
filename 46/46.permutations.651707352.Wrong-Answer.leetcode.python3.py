class Solution:
    def permute(self, nums, ret=[], permutation=[]):
        if not nums:
            print("permutation --> %s" % permutation)
            print("ret --> %s" % ret)
            ret.append(permutation)
            print("ret --> %s" % ret)
        for i in range(len(nums)):
            self.permute(nums[:i] + nums[i + 1:], ret, permutation + [nums[i]])
        return ret

