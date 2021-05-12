class Solution(object):
    def lengthOfLIS(self, nums):
        LIS = []
        for num in nums:
            list_nb = self.binary_search(num, LIS)
            if list_nb == len(LIS) - 1:
                LIS.append(num)
            else:
                LIS[list_nb + 1] = min(num, LIS[list_nb + 1])
        return len(LIS)

