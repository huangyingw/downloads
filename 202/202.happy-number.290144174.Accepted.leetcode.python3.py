class Solution:
    def isHappy(self, n: int) -> bool:
        temp = set()
        while n:
            if n == 1:
                return True
            temp.add(n)
            new_no = self.squareSum(n)
            if new_no in temp:
                return False
            n = new_no

    def squareSum(self, n):
        new_no = 0
        while n:
            new_no += (n % 10) * (n % 10)
            n //= 10
        return new_no

