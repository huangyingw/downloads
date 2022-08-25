class Solution(object):
    def maxProduct(self, nums):
        result = float('-inf')
        local = 1
        for num in nums:
            local = max(local * num, num)
            print("local --> %s" % local)
            result = max(result, local)
            print("result --> %s" % result)
        return result

