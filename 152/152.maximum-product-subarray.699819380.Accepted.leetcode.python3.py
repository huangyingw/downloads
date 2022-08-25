class Solution(object):
    def maxProduct(self, nums):
        largest_product = float('-inf')
        most_neg, most_pos = 1, 1
        for num in nums:
            most_pos, most_neg = max(num, most_pos * num, most_neg * num), min(num, most_pos * num, most_neg * num)
            largest_product = max(largest_product, most_pos, most_neg)
        return largest_product

