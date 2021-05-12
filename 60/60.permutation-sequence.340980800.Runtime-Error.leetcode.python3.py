class Solution(object):
    def getPermutation(self, n, k):
        ret = []
        return self.dfs(range(n), ret, [], k)

    def dfs(self, nums, ret, permutation, k):
        if not nums:
            ret.append(permutation)
            if len(ret) == k:
                return permutation
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], ret, permutation + [nums[i]], k)

