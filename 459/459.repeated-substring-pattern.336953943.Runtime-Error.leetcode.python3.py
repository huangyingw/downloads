class Solution(object):
    def repeatedSubstringPattern(self, s):
        result = ""
        for i in range(len(s) // 2, 1, -1):
            if n % i == 0:
                for j in range(n // i):
                    result += s[0:i]
        return s == result

