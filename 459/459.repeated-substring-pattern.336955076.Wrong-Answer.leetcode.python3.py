class Solution(object):
    def repeatedSubstringPattern(self, s):
        result = ""
        for i in range(len(s) // 2, 1, -1):
            if len(s) % i == 0:
                result = ""
                for j in range(len(s) // i):
                    newStr = s[0:i]
                    print('newStr --> %s' % newStr)
                    result += newStr
        print('result --> %s' % result)
        return s == result

