class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        count = start = 0
        while count < len(nums):
            cur = start
            prev = nums[start]
            while 1:
                nextt = (cur + k) % len(nums)
                nums[nextt], prev = prev, nums[nextt]
                cur = nextt
                count += 1
                if start == cur:
                    break
            start += 1

