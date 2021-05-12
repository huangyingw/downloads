class Solution:
    def longestPalindrome(self, s):
        res = 0
        flag = 0
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for c in count.values():
            if c % 2 == 0:
                res += c
            else:
                res += c - 1
                flag = 1
        if flag == 1:
            return res + 1
        return res

