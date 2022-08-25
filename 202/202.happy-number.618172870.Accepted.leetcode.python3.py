class Solution:
    def isHappy(self, n: int) -> bool:
        temp = set()
        while n > 1:
            temp.add(n)
            new_no = self.squareSum(n)
            if new_no in temp:
                return False
            n = new_no
        return True

    def squareSum(self, n):
        new_no = 0
        while n:
            new_no += (n % 10) * (n % 10)
            n //= 10
        return new_no

