class Solution(object):
    def wordBreak(self, s, wordDict):
        self.result = []
        self.dfs(s, wordDict, '')
        return self.result

    def dfs(self, s, wordDict, currStr):
        if self.check(s, wordDict):
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, currStr + ' ' + s[:i])

    def check(self, s, wordDict):
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s)):
            for j in range(i, -1, -1):
                if dp[j] and s[j:i + 1] in wordDict:
                    dp[i + 1] = True
                    break

        return dp[len(s)]

