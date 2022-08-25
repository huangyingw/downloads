class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            print("return --> 1")
            return ""
        if len(strs) == 1:
            print("return --> 2")
            return strs[0]
        strs.sort()
        length = min(len(strs[0]), len(strs[-1]))
        ch = ""
        for i in range(length):
            if strs[0][i] == strs[-1][i]:
                ch += strs[0][i]
        return ch

