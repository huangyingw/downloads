class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabets = {}
        for idx, ch in enumerate(s):
            if ch not in alphabets:
                alphabets[ch] = [0, idx]
            alphabets[ch][0] += 1
        for key, value in alphabets.items():
            if value[0] == 1:
                return value[1]
        return -1

