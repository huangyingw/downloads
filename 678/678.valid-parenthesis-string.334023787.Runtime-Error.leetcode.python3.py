class Solution(object):
    def checkValidString(self, s):
        L = ['(', '*']
        R = [')', '*']
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s)):
            dp[i][i] = True if s[i] == '*'
            if df[i + 1][j - 1] and s[i] in L and s[j] in R:
                dp[i][j] = True
            for k in range(i, j):
                if dp[i][k] and dp[k + 1][j]:
                    dp[i][j] = True
                    break
        return dp[0][len(s) - 1]

