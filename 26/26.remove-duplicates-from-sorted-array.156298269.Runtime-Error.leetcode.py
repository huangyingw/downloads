class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        for num in nums:
            if nums[index - 1] != num:
                nums[index] = num
                index += 1
        return index

