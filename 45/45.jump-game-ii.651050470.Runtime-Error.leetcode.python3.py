class Solution(object):
    def jump1(self, nums):
        jumps = 0
        current_jump_max = 0
        previous_jump_max = 0
        for i in range(len(nums) - 1):
            current_jump_max = max(current_jump_max, i + nums[i])
            if i == previous_jump_max:
                jumps += 1
                previous_jump_max = current_jump_max
        return jumps

    def jump2(self, nums):
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

