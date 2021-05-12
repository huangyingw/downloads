class Solution(object):
    def removeElement(self, nums, val):
        rm_index = []
        for idx in xrange(len(nums)):
            if nums[idx] == val:
                rm_index.append(idx)
        last = len(nums) - 1
        for idx in rm_index:
            while last >= 0 and nums[last] == val:
                last -= 1
            if last < 0:
                break
            nums[idx] = nums[last]
            last -= 1
        return len(nums) - len(rm_index)

