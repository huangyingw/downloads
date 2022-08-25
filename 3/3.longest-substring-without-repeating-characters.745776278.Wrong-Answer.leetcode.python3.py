class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mapSet = {}
        start, result = 0, 0
        for end in range(len(s)):
            print("s[end] --> %s" % s[end])
            if s[end] in mapSet:
                start = max(mapSet[s[end]], start)
                print("start --> %s" % start)
            print("end --> %s" % end)
            result = max(result, end - start + 1)
            print("result --> %s" % result)
            mapSet[s[end]] = end
        return result

