class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
        return rev // 10 == x or rev == x

