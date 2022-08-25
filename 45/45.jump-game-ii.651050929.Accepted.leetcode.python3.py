class Solution(object):
    def jump(self, nums):
        jumps = 0
        current_jump_max = 0
        previous_jump_max = 0
        for i in range(len(nums) - 1):
            current_jump_max = max(current_jump_max, i + nums[i])
            if i == previous_jump_max:
                jumps += 1
                previous_jump_max = current_jump_max
        return jumps

