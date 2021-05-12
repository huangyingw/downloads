class Solution(object):
    def missingElement(self, nums, k):
        nums.append(float("inf"))
        prev = nums[0]
        for num in nums[1:]:
            missing = num - prev
            if k - missing <= 0:
                return prev + k
            k -= missing
            prev = num

