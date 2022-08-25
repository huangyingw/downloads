class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charMap = {}
        for i in range(256):
            charMap[i] = -1
        i = max_len = 0
        for j in range(len(s)):
            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1
            charMap[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
        return max_len

