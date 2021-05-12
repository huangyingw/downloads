class Solution:
    def kLengthApart(self, nums, k):
        one_place = None
        for i in range(len(nums)):
            if nums[i] == 1:
                if one_place and i - one_place < k:
                    return False
                one_place = i + 1
        return True

