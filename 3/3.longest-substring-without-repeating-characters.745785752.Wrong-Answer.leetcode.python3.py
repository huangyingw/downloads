class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mapSet = {}
        start, result = 0, 0
        for end in range(len(s)):
            if s[end] in mapSet:
                print("end --> %s" % end)
                print("s[end] --> %s" % s[end])
                print("mapSet[s[end]] --> %s" % mapSet[s[end]])
                start = max(mapSet[s[end]], end)
                print("start --> %s" % start)
            result = max(result, end - start + 1)
            print("result --> %s" % result)
            mapSet[s[end]] = end
        return result

