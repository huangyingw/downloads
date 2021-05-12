class Solution:
    def numDecodings(self, s):
        f0 = 0
        e0, e1, e2 = 1, 0, 0
        for c in s:
            f0 = (c > '0') * e0 + e1 + e2 * (c < '7')
            e1 = e0 if c == '1' else 0
            e2 = e0 if c == '2' else 0
            e0 = f0
        return f0

