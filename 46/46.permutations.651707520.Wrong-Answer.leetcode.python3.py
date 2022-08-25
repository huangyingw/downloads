class Solution:
    def permute(self, nums, ret=[], permutation=[]):
        print("ret --> %s" % ret)
        if not nums:
            print("permutation --> %s" % permutation)
            ret.append(permutation)
            print("ret --> %s" % ret)
        for i in range(len(nums)):
            self.permute(nums[:i] + nums[i + 1:], ret, permutation + [nums[i]])
        return ret

