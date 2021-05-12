class Solution(object):
    def generatePossibleNextMoves(self, s):
        result = []
        for i in range(len(s) - 1):
            if s[i:i + 2] == "++":
                result.append(s[:i] + "--" + s[i + 2:])
        return result

