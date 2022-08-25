class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for index in range(len(nums) - 2):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                if left - 1 > index and nums[left] == nums[left - 1]:
                    left += 1
                elif right + 1 <= len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                elif nums[index] + nums[left] + nums[right] == 0:
                    result += [[nums[index], nums[left], nums[right]]]
                    left += 1
                    right -= 1
                elif nums[index] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return result

