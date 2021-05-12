class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 0, num
        while start <= end:
            mid = (start + end) // 2

            square = mid * mid
            if square == num:
                return True
            elif square > num:
                end = mid - 1
            else:
                start = mid + 1

        return False

