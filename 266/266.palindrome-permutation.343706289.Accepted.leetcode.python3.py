class Solution(object):
    def canPermutePalindrome(self, s):
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        odd = 0
        for c in dic:
            if dic[c] % 2 != 0:
                odd += 1
        return odd <= 1

