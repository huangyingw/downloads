class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for j in range(1, len(s) + 1):
            for i in range(j):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[len(s)]

