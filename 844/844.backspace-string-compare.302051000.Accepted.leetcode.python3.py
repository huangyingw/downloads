class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        s_skip = t_skip = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    s_skip += 1
                    i -= 1
                elif s_skip > 0:
                    s_skip -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == '#':
                    t_skip += 1
                    j -= 1
                elif t_skip > 0:
                    t_skip -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True

