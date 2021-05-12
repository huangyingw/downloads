class Solution(object):
    def generatePossibleNextMoves(self, s):
        return [(s[:i] + "--" + s[i + 2:]) for i in range(len(s)) if s[i:i + 2] == "++"]

