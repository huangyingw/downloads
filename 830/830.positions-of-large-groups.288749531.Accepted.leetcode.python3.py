class Solution:
    def largeGroupPositions(self, S):
        i, j, n, res = 0, 0, len(S), []
        while j < n:
            while j < n and S[i] == S[j]:
                j += 1
            if j - i >= 3:
                res.append((i, j - 1))
            i = j
        return res

