class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        s_skip = t_skip = 0
        while i >= 0 or j >= 0:
            while i >= 0 and (s_skip or S[i] == '#'):
                s_skip += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (t_skip or T[j] == '#'):
                t_skip += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i -= 1
            j -= 1
        return True

