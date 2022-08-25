class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        length = min(len(strs[0]), len(strs[-1]))
        ch = ""
        for i in range(0, length):
            if strs[0][i] == strs[-1][i]:
                ch += strs[0][i]
            else:
                return ch
        return ch

