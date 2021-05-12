class Solution:
    def removeDuplicates(self, nums):
        idx = 0
        for n in nums[1:]:
            if n != nums[idx]:
                idx += 1
                nums[idx] = n
        return idx + 1

