class Solution(object):
    def removeElement(self, nums, val):
        rm_index = []
        for i in xrange(len(nums)):
            if nums[i] == val:
                rm_index.append(i)
        last = len(nums) - 1
        for i in rm_index:
            while last >= 0 and nums[last] == val:
                last -= 1
            if last < 0:
                break
            nums[i] = nums[last]
            last -= 1
        return len(nums) - len(rm_index)

