class Solution(object):
    def letterCasePermutation(self, S):
        ret = []
        self.dfs(S, , 0, ret, [])
        return ret

    def dfs(self, S, idx, ret, permutation):
        if not S:
            ret.append(permutation)
        if S[idx].isalpha():
            self.dfs(S, idx + 1, ret, permutation + [S[idx].upper()])
            self.dfs(S, idx + 1, ret, permutation + [S[idx].lower()])
        else:
            self.dfs(S, idx + 1, ret, permutation + [S[idx]])

