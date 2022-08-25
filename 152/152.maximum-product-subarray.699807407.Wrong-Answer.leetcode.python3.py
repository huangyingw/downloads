class Solution(object):
    def maxProduct(self, nums):
        largest_product = float('-inf')
        most_neg, most_pos = 1, 1
        for num in nums:
            most_pos = max(num, most_pos * num, most_neg * num)
            most_neg = min(num, most_pos * num, most_neg * num)
            largest_product = max(largest_product, most_pos, most_neg)
        return largest_product

