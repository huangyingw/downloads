class Solution(object):
    def repeatedSubstringPattern(self, s):
        result = ""
        for i in range(len(s) // 2, 1, -1):
            if len(s) % i == 0:
                for j in range(len(s) // i):
                    result += s[0:i]
        return s == result

