class Solution(object):
    def maxProduct(self, nums):
        result = 0
        local = 1
        for num in nums:
            local *= num
            print("local --> %s" % local)
            result = max(result, local)
            print("result --> %s" % result)
        return result

