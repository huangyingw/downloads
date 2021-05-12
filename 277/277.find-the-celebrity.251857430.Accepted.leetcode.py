class Solution(object):
    def findCelebrity(self, n):
        left, right = 0, n - 1
        while left < right:
            if knows(left, right):
                left += 1
            else:
                right -= 1
        for idx in range(n):
            if not knows(idx, left):
                return -1
            if idx != left and knows(left, idx):
                return -1
        return left

