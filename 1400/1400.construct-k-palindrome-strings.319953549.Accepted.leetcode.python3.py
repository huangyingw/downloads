class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) <= k:
            return len(s) == k

        alphabets = {}
        for c in s:
            alphabets[c] = alphabets.get(c, 0) + 1

        count = sum(value % 2 for value in alphabets.values())

        return count <= k

