class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if self.isValid(i) and self.isValid(n - i):
                return [i, n - i]

    def isValid(self, n):
        while n:
            if n % 10 == 0:
                return False
            n //= 10
        return True

