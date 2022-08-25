class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        start = 0
        longest = 0
        for i, c in enumerate(s):
            print("i --> %s" % i)
            print("c --> %s" % c)
            print("last_seen --> %s" % last_seen)
            if c in last_seen:
                start = max(start, last_seen[c] + 1)
                print("start --> %s" % start)
                longest = max(longest, i - start + 1)
            else:
                longest = max(longest, i - start + 1)
                print("longest --> %s" % longest)
            last_seen[c] = i
            print()
        return longest

