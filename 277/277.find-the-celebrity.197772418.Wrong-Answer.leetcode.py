class Solution(object):
    def findCelebrity(self, n):
        print("n --> %s" % n)
        left, right = 0, n - 1
        print("left --> %s" % left)
        print("right --> %s" % right)

        while left < right:
            if knows(left, right):
                left += 1
            else:
                right -= 1

        print("left --> %s" % left)
        for idx in range(n):
            if not knows(idx, left):
                return -1

            if knows(left, idx):
                return -1

        return left

