class Solution:
    def titleToNumber(self, s):
        return reduce(lambda x, y: x * 26 + y, [ord(c) - ord('A') + 1 for c in s])

