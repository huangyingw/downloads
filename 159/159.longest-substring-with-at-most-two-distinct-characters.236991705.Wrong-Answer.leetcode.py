class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        start, max_substring = 0, 0
        last_seen = {}                  # key is char, value is last index of char

        for i, c in enumerate(s):
            if c in last_seen or len(last_seen) < 2:    # extend substring with same start
                max_substring = max(max_substring, i - start + 1)
            last_seen[c] = i
        return max_substring

