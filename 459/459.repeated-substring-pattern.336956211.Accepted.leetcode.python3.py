class Solution(object):
    def repeatedSubstringPattern(self, s):
        for i in range(len(s) // 2, 0, -1):
            if len(s) % i == 0:
                result = ""
                for j in range(len(s) // i):
                    result += s[0:i]
                    if s == result:
                        return True
        return False

