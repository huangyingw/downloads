class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabets = {}
        for c in s:
            alphabets[c] = alphabets.get(c, 0) + 1
        for i in range(len(s)):
            if alphabets.get(s[i]) == 1:
                return i
        return -1

