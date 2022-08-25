class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mapSet = {}
        start, result = 0, 0
        for end in range(len(s)):
            if s[end] in mapSet:
                start = max(mapSet[s[end]], start)
                print("start --> %s" % s[start])
            result = max(result, end - start + 1)
            print("result --> %s" % result)
            mapSet[s[end]] = end
        return result

