class Solution(object):
    def missingElement(self, nums, k):
        nums.append(float("inf"))
        prev = nums[0]
        for num in nums[1:]:
            missing = num - prev
            k -= missing
            if k <= 0:
                return prev + 1
            prev = num

