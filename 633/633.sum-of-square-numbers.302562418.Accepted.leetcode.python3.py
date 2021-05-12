class Solution:
    def judgeSquareSum(self, c):
        def is_square(N):
            return int(N**.5)**2 == N
        for a in range(int(c**.5) + 1):
            if is_square(c - a * a):
                return True
        return False

