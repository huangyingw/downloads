class Solution:
    def canJump(self, nums):

        memo = [0] * len(nums)
        memo[-1] = 1

        def canJumpFromPosition(position, nums):
            if memo[position] != 0:
                return True if memo[position] == 1 else False
            furthestJump = min(position + nums[position], len(nums) - 1)
            for i in range(position + 1, furthestJump + 1):
                if canJumpFromPosition(i, nums):
                    memo[position] = 1
                    return True
            memo[position] = -1
            return False
        return canJumpFromPosition(0, nums)


class Solution2:
    def canJump(self, nums):
        memo = [0] * len(nums)
        memo[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            furthest = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthest + 1):
                if memo[j] == 1:
                    memo[i] = 1
                    break
        return memo[0] == 1


class Solution3:
    def canJump(self, nums):
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0
    t = Solution3()

