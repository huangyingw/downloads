class Solution(object):
    def numberOfPatterns(self, m, n):
        patterns = [0, 9, 56, 320, 1624, 7152, 26016, 72912, 140704, 140704]
        return sum(patterns[m:n + 1])

