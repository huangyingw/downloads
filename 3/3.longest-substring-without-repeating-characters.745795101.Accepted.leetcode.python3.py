class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        start = 0
        longest = 0
        for i, c in enumerate(s):
            if c in last_seen:
                start = max(start, last_seen[c] + 1)
                print("start --> %s" % start)
            longest = max(longest, i - start + 1)
            last_seen[c] = i
        return longest

