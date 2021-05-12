class Solution(object):
    def singleNumber(self, nums):
        if not nums:
            return -1

        if len(nums) == 1:
            return nums[0]

        nums.sort()
        j = 1

        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                j += 1
            else:
                if j < 3:
                    return nums[i]

                j = 1

        return nums[-1]

