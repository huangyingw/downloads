class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            return True
        return False

