class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = res = 0
        for c in s:
            count += 1 if c == 'L' else -1
            res += count == 0
        return res

