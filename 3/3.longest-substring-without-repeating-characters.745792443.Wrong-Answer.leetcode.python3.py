class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mapSet = {}
        start, result = 0, 0
        for end in range(len(s)):
            if s[end] in mapSet:
                start = max(mapSet[s[end]], start)
            result = end - start + 1
            mapSet[s[end]] = end
        return result

