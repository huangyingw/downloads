class Solution(object):
    def threeSumSmaller(self, nums, target):
        count = 0
        nums.sort()
        for idx in range(len(nums)):
            left, right = idx + 1, len(nums) - 1
            while left < right:
                if nums[idx] + nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count

