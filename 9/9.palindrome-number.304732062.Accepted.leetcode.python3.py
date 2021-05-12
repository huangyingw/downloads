
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        temp, rev = x, 0
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp //= 10
        return True if x == rev else False

    def isPalindrome_alternative(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = (rev * 10) + (x % 10)
            x //= 10

        return rev == x or rev // 10 == x

