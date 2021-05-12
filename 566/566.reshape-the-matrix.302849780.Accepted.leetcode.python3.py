class Solution(object):
    def matrixReshape(self, nums, r, c):
        if r * c != len(nums) * len(nums[0]):
            return nums
        else:
            items = [y for x in nums for y in x]
            return [items[x * c: ((x + 1) * c)] for x in range(r)]

