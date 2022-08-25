class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        if (len(nums) >= 3) and (nums[0] == nums[len(nums) - 1]) and (nums[0] == 0):
            return [[0, 0, 0]]
        result = []
        for index in range(len(nums) - 1):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                if left - 1 >= index + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                if right + 1 <= len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue
                currSum = nums[index] + nums[left] + nums[right]
                if currSum == 0:
                    result += [[nums[index], nums[left], nums[right]]]
                    left += 1
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1
        return result

