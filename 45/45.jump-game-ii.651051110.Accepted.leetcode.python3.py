class Solution(object):
    def jump(self, nums):
        ans, n = 0, len(nums)
        i, e = 0, 0
        while e < n - 1:
            p = e
            while i <= p:
                if i + nums[i] > e:
                    e = i + nums[i]
                i += 1
            if p == e:
                return -1
            ans += 1
        return ans

