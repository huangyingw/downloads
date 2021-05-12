class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        start, end, counter, ret = 0, 0, 0, 0
        counts = {}
        while end < len(s):
            c = s[end]
            counts[c] = counts.get(c, 0) + 1
            if counts[c] == 1:
                counter += 1
            end += 1
            while counter > 2:
                c2 = s[start]
                counts[c2] -= 1
                start += 1
            ret = max(ret, end - start)
        return ret

