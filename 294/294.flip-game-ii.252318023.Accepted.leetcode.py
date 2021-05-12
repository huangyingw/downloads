class Solution(object):
    def canWin(self, s):
        for i in range(len(s)):
            if s[i:i + 2] == '++' and not self.canWin(s[:i] + '--' + s[i + 2:]):
                return True
        return False

