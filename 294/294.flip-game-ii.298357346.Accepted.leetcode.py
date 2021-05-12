class Solution(object):
    def canWin(self, s, memo={}):
        if s in memo:
            return memo[s]
        for i in range(len(s) - 1):
            if s[i:i + 2] == '++' and not self.canWin(s[:i] + '--' + s[i + 2:]):
                memo[s] = True
                return True
        memo[s] = False
        return False

