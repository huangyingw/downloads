class Solution(object):
    def findNumbers(self, nums):

        return len([num for num in nums if len(str(num)) % 2 == 0])

