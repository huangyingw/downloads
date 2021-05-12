class Solution(object):
    def majorityElement(self, nums):
        count = 0
        result = nums[0]

        for num in nums:
            if count == 0:
                result = num

            if result == num:
                count += 1
            else:
                count -= 1
        return result

