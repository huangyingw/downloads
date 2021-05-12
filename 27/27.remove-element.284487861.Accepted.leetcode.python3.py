class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        i = 0
        while i < n:
            item = nums.pop(0)
            i += 1
            if item != val:
                nums += [item]
        return len(nums)

