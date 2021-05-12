import string


class Solution(object):
    def isPalindrome(self, s):
        allowed = set(string.ascii_lowercase + string.digits)
        s = [c for c in s.lower() if c in allowed]
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

