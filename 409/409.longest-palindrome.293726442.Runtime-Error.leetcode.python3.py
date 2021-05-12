class Solution:
    def longestPalindrome(self, s):
        ans = 0
        char_map = {}
        for c in s:
            char_map[c] = char_map.get(c, 0) + 1
        for c in char_map.keys():
            if char_map[c] % 2 == 0:
                ans += char_map.pop(c)
            else:
                ans += char_map[c] / 2 * 2
        if len(char_map) != 0:
            ans += 1
        return ans

