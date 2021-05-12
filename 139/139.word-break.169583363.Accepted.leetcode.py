class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for start in range(len(s)):
            if dp[start]:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in wordDict:
                        dp[end] = True

        return dp[len(s)]

