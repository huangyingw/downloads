class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        left, right = 1, x
        while left < right:
            mid = (left + right) // 2
            squared = mid * mid
            if squared == x:
                return mid
            elif squared > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

