class Solution:
    def ambiguousCoordinates(self, S):
        S = S[1:-1]
        res = []
        for i in range(1, len(S)):
            left = self.point(S[:i])
            right = self.point(S[i:])
            for l in left:
                for r in right:
                    res.append("(" + l + ", " + r + ')')
        return res

    def point(self, s):
        if s[0] == '0' and s[-1] == '0':
            return ['0'] if s == '0' else []
        if s[-1] == '0':
            return [s]
        if s[0] == '0':
            return [s[0] + '.' + s[1:]]
        return [s[:i] + '.' + s[i:] for i in range(1, len(s))] + [s]

