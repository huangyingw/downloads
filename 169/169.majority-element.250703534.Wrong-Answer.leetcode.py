class Solution(object):
    def majorityElement(self, nums):
        count, result = 0, nums[0]
        for num in nums:
            if count == 0:
                result = num
            elif result == num:
                count += 1
            else:
                count -= 1
        return result

