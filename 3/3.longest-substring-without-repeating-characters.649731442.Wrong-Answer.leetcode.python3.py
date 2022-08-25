class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        start = 0
        longest = 0
        for i, c in enumerate(s):
            if c in last_seen:
                start = max(start, last_seen[c] + 1)
                print("start --> %s" % start)
            else:
                print("i --> %s" % i)
                longest = max(longest, i - start + 1)
                print("longest --> %s" % longest)
            last_seen[c] = i
            print()
        return longest

