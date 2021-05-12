class Solution(object):
    def threeSum(self, nums):
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for index in range(0, len(nums) - 2):
            if index - 1 >= 0 and nums[index] == nums[index - 1]:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                if right + 1 < len(nums) and nums[right] == nums[right + 1]:
                    right -= 1
                elif left - 1 > index and nums[left] == nums[left - 1]:
                    left += 1
                elif nums[index] + nums[left] + nums[right] == 0:
                    result += [[nums[index], nums[left], nums[right]]]
                    right -= 1
                    left += 1
                elif nums[index] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return result

