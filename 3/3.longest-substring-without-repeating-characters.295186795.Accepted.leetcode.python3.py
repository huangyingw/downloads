class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        max_length = 0
        lower_limit = 0
        for i in range(len(s)):
            if s[i] in d:
                lower_limit = max(d.get(s[i]), lower_limit)
            max_length = max(max_length, i - lower_limit + 1)
            d[s[i]] = i + 1
        return max_length

