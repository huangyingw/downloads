class Solution(object):
    def longestCommonPrefix(self, strs):
        minStr = min(strs, key=len)
        for index in range(len(minStr)):
            for str in strs:
                if str[index] != minStr[index]:
                    return minStr[:index]
        return minStr

