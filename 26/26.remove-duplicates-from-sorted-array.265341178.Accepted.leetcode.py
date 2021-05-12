class Solution(object):
    def removeDuplicates(self, nums):
        index = 1
        for nav in range(1, len(nums)):
            if nums[nav] != nums[index - 1]:
                nums[index] = nums[nav]
                index += 1
        return index

