class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        prev, curr = 1, 2
        while curr < len(nums):
            if nums[prev] != nums[curr] or nums[curr] != nums[prev - 1]:
                prev += 1
                nums[prev] = nums[curr]
            curr += 1
        return prev + 1

