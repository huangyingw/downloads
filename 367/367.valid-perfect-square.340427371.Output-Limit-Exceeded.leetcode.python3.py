class Solution(object):
    def isPerfectSquare(self, num):
        left, right = 0, num + 1
        while left <= right:
            mid = (left + right) // 2
            print('mid --> %s' % mid)
            square = mid * mid
            if square == num:
                return True
            if square > num:
                right = mid
            else:
                left = mid + 1
        return False

