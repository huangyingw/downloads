class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.squareSum(self.squareSum(n))
        while fast != slow:
            slow = self.squareSum(slow)
            fast = self.squareSum(self.squareSum(fast))
        return fast == 1

    def squareSum(self, n):
        new_no = 0
        while n:
            new_no += (n % 10) * (n % 10)
            n //= 10
        return new_no

