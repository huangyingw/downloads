class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        start = 0
        end = len(s) - 1
        while start < end:
            if not 'a' <= s[start] <= 'z':
                start += 1
            elif not 'a' <= s[end] <= 'z':
                end -= 1
            elif s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True

