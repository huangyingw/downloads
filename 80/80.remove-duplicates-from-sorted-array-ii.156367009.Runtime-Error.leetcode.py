class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 2
        for nav in range(3, len(nums)):
            if nums[index - 2] != nums[nav]:
                nums[index] = nums[nav]
                index += 1
        return index

