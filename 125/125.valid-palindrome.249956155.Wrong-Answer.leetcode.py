class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        start = 0
        end = len(s) - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
            if not s[end].isalnum():
                end -= 1
            elif s[start] != s[end]:
                print('start --> %s' % start)
                print('s[start] --> %s' % s[start])
                print('end --> %s' % end)
                print('s[end] --> %s' % s[end])
                return False
            else:
                start += 1
                end -= 1
        return True

