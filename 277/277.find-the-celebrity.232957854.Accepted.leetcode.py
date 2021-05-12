class Solution(object):
    def findCelebrity(self, n):
        left, right = 0, n - 1

        while left < right:
            if knows(left, right):
                left += 1
            else:
                right -= 1

        for idx in range(n):
            if idx == left:
                continue

            if not knows(idx, left):
                return -1

            if knows(left, idx):
                return -1

        return left

